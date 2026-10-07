from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User, Event, Booking, Ticket
from app.schemas import BookingCreate, BookingResponse
from app.services.booking_service import calculate_total_price
from app.services.ticket_service import (
    generate_ticket_code,
    generate_qr_code
)
from app.services.notification_service import create_notification


router = APIRouter(
    prefix="/api/v1/bookings",
    tags=["Bookings"]
)


@router.post(
    "/",
    response_model=BookingResponse,
    status_code=201
)
def create_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(
        Event.id == booking_data.event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    if event.available_tickets < booking_data.ticket_quantity:
        raise HTTPException(
            status_code=400,
            detail="Not enough tickets available"
        )

    total_price = calculate_total_price(
        event.ticket_price,
        booking_data.ticket_quantity
    )

    booking = Booking(
        user_id=current_user.id,
        event_id=event.id,
        ticket_quantity=booking_data.ticket_quantity,
        total_price=total_price,
        booking_status="CONFIRMED"
    )

    event.available_tickets -= booking_data.ticket_quantity

    db.add(booking)
    db.flush()

    # Generate unique ticket code
    ticket_code = generate_ticket_code()

    # Generate QR image
    qr_code_url = generate_qr_code(ticket_code)

    # Create ticket
    ticket = Ticket(
        booking_id=booking.id,
        ticket_code=ticket_code,
        qr_code_url=qr_code_url
    )

    db.add(ticket)

    create_notification(
    db=db,
    user_id=current_user.id,
    title="Booking Confirmed",
    message=(
        f"Your booking for '{event.title}' has been confirmed. "
        f"You booked {booking.ticket_quantity} ticket(s). "
        f"Total amount: ₹{booking.total_price:.2f}."
    ),
    notification_type="BOOKING"
)

    db.commit()

    db.refresh(booking)

    return booking


@router.get(
    "/",
    response_model=list[BookingResponse]
)
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Booking).filter(
        Booking.user_id == current_user.id
    ).order_by(
        Booking.created_at.desc()
    ).all()


@router.get(
    "/{booking_id}",
    response_model=BookingResponse
)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == current_user.id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking