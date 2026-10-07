
from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict
)


# =========================================================
# USER / AUTHENTICATION
# =========================================================

class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class LoginRequest(BaseModel):
    email: EmailStr

    password: str = Field(
        min_length=1,
        max_length=100
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# =========================================================
# EVENTS
# =========================================================

class EventCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200
    )

    description: Optional[str] = None

    category: str

    location: str

    event_date: datetime

    ticket_price: float = Field(
        gt=0
    )

    total_tickets: int = Field(
        gt=0
    )

    banner_image: Optional[str] = None


class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    category: str
    location: str
    event_date: datetime
    ticket_price: float
    total_tickets: int
    available_tickets: int
    banner_image: Optional[str]
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# BOOKINGS
# =========================================================

class BookingCreate(BaseModel):
    event_id: int

    ticket_quantity: int = Field(
        gt=0,
        le=10
    )


class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    ticket_quantity: int
    total_price: float
    booking_status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# TICKETS
# =========================================================

class TicketResponse(BaseModel):
    id: int
    booking_id: int
    ticket_code: str
    qr_code_url: Optional[str]
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# NOTIFICATIONS
# =========================================================

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    type: str
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

