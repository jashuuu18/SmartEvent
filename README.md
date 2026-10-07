
# SmartEvent – Event Discovery & Ticket Booking System

SmartEvent is a full-stack event discovery and ticket booking application built using **FastAPI, SQLite, React, and JWT authentication**.

## Features

### Authentication

* User registration and login
* JWT authentication
* Password hashing with bcrypt
* Protected routes
* User profile

### Event Discovery

* View upcoming events
* Search events
* Filter by category
* View complete event details
* Display ticket price and availability

### Ticket Booking

* Book event tickets
* Select ticket quantity
* Automatic total price calculation
* Ticket availability validation
* Sold-out prevention
* Booking history
* Booking confirmation

### QR Tickets

* Automatic ticket generation after booking
* Unique ticket code
* QR code generation
* My Tickets page

### Notifications

* Booking confirmation notification
* View notifications
* Unread notification count
* Mark notification as read

### Frontend

* React with Vite
* React Router
* Axios
* JWT token handling
* Protected routes
* Responsive UI
* Toast notifications

## Technologies

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT
* Passlib
* bcrypt
* QRCode

### Frontend

* React
* Vite
* JavaScript
* React Router
* Axios
* React Toastify
* CSS

## Project Structure

```text
SmartEvent/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── dependencies.py
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   │
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── events.py
│   │   │   ├── bookings.py
│   │   │   ├── tickets.py
│   │   │   └── notifications.py
│   │   │
│   │   ├── services/
│   │   │   ├── booking_service.py
│   │   │   ├── ticket_service.py
│   │   │   └── notification_service.py
│   │   │
│   │   └── static/
│   │       └── qr_codes/
│   │
│   ├── .env
│   ├── requirements.txt
│   └── smart_event.db
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── EventCard.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   │
│   │   ├── context/
│   │   │   └── AuthContext.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── EventDetails.jsx
│   │   │   ├── BookingConfirmation.jsx
│   │   │   ├── BookingHistory.jsx
│   │   │   ├── Tickets.jsx
│   │   │   ├── Notifications.jsx
│   │   │   └── Profile.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   └── package.json
│
└── README.md
```

## Backend Setup

Open PowerShell:

```powershell
cd "C:\Users\G . Jaswanth\SmartEvent\backend"
```

Activate the virtual environment:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the FastAPI server:

```powershell
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

Open another PowerShell:

```powershell
cd "C:\Users\G . Jaswanth\SmartEvent\frontend"
```

Install dependencies:

```powershell
npm install
```

Start React:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Main API Modules

| Module         | Endpoint                |
| -------------- | ----------------------- |
| Authentication | `/api/v1/auth`          |
| Users          | `/api/v1/users`         |
| Events         | `/api/v1/events`        |
| Bookings       | `/api/v1/bookings`      |
| Tickets        | `/api/v1/tickets`       |
| Notifications  | `/api/v1/notifications` |

## Booking Flow

```text
Login
   ↓
Browse Events
   ↓
Select Event
   ↓
Choose Tickets
   ↓
Book Tickets
   ↓
Booking Confirmed
   ↓
Ticket + QR Code Generated
   ↓
Notification Created
   ↓
View My Tickets / My Bookings
```

## Security

* JWT-based authentication
* Password hashing
* Protected API endpoints
* Protected React routes
* User ownership validation
* Pydantic request validation
* Centralized exception handling

## Testing Checklist

* [ ] User registration
* [ ] User login
* [ ] JWT authentication
* [ ] Protected routes
* [ ] Event listing
* [ ] Event search
* [ ] Category filtering
* [ ] Event details
* [ ] Ticket booking
* [ ] Ticket availability
* [ ] Booking confirmation
* [ ] Booking history
* [ ] QR ticket
* [ ] Notifications
* [ ] Mark notification as read
* [ ] Profile
* [ ] Logout
* [ ] Responsive frontend

## Project Status

SmartEvent provides a complete event discovery and ticket booking workflow with authentication, booking management, QR tickets, notifications, and a React-based responsive frontend.
