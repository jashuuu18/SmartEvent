from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Event,
    Booking,
    Ticket,
    Notification
)
from app.schemas import EventCreate, EventResponse


router = APIRouter(
    prefix="/api/v1/events",
    tags=["Events"]
)


@router.post(
    "/",
    response_model=EventResponse,
    status_code=201
)
def create_event(
    event_data: EventCreate,
    db: Session = Depends(get_db)
):
    event = Event(
        title=event_data.title,
        description=event_data.description,
        category=event_data.category,
        location=event_data.location,
        event_date=event_data.event_date,
        ticket_price=event_data.ticket_price,
        total_tickets=event_data.total_tickets,
        available_tickets=event_data.total_tickets,
        banner_image=event_data.banner_image
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


@router.get(
    "/",
    response_model=list[EventResponse]
)
def get_events(
    category: Optional[str] = Query(default=None),
    search: Optional[str] = Query(default=None),
    db: Session = Depends(get_db)
):
    query = db.query(Event)

    if category:
        query = query.filter(
            Event.category.ilike(category)
        )

    if search:
        query = query.filter(
            Event.title.ilike(f"%{search}%")
        )

    return query.order_by(
        Event.event_date.asc()
    ).all()


@router.get(
    "/{event_id}",
    response_model=EventResponse
)
def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    bookings = db.query(Booking).filter(
        Booking.event_id == event_id
    ).all()

    for booking in bookings:

        ticket = db.query(Ticket).filter(
            Ticket.booking_id == booking.id
        ).first()

        if ticket:
            db.delete(ticket)

        notification_message = (
            f"Your booking for '{event.title}'"
        )

        notifications = db.query(Notification).filter(
            Notification.user_id == booking.user_id,
            Notification.message.like(
                f"{notification_message}%"
            )
        ).all()

        for notification in notifications:
            db.delete(notification)

        db.delete(booking)

    db.delete(event)

    db.commit()

    return {
        "success": True,
        "message": f"Event {event_id} deleted successfully"
    }