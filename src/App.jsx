import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import { AuthProvider } from "./context/AuthContext.jsx";
import Navbar from "./components/Navbar.jsx";

import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import EventDetails from "./pages/EventDetails.jsx";
import BookingHistory from "./pages/BookingHistory.jsx";
import Tickets from "./pages/Tickets.jsx";
import Notifications from "./pages/Notifications.jsx";
import BookingConfirmation from "./pages/BookingConfirmation.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import Profile from "./pages/Profile.jsx";


function App() {
  return (
    <BrowserRouter>
      <AuthProvider>

        <Navbar />

        <Routes>

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/login"
            element={<Login />}
          />

          <Route
            path="/register"
            element={<Register />}
          />

          <Route
            path="/events/:eventId"
            element={<EventDetails />}
          />

          <Route
            path="/booking-confirmation/:bookingId"
            element={
            <ProtectedRoute>
            <BookingConfirmation />
             </ProtectedRoute>
            }
          />

          <Route
            path="/profile"
            element={
            <ProtectedRoute>
            <Profile />
            </ProtectedRoute>
           }
          />


          <Route
            path="/bookings"
            element={
            <ProtectedRoute>
             <BookingHistory />
            </ProtectedRoute>
            }
          />

          <Route
            path="/tickets"
            element={
            <ProtectedRoute>
            <Tickets />
            </ProtectedRoute>
             }
          />

           <Route
             path="/notifications"
             element={
            <ProtectedRoute>
            <Notifications />
            </ProtectedRoute>
            }
          />

        </Routes>

        <ToastContainer position="top-right" />

      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;