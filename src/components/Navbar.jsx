import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

import { useAuth } from "../context/AuthContext.jsx";
import api from "../services/api";

function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const [unreadCount, setUnreadCount] = useState(0);

  useEffect(() => {
    if (!user) {
      setUnreadCount(0);
      return;
    }

    fetchUnreadNotifications();
  }, [user]);

  const fetchUnreadNotifications = async () => {
    try {
      const response = await api.get("/notifications/");

      const unread = response.data.filter(
        (notification) => !notification.is_read
      );

      setUnreadCount(unread.length);
    } catch (error) {
      console.error(
        "Error loading notification count:",
        error
      );
    }
  };

  const handleLogout = () => {
    logout();

    setUnreadCount(0);

    toast.success("Logged out successfully.");

    navigate("/");
  };

  return (
    <nav className="navbar">

      <Link to="/" className="logo">
        SmartEvent
      </Link>

      <div className="nav-links">

        <Link to="/">
          Home
        </Link>

        {user ? (
          <>
            <Link to="/bookings">
              My Bookings
            </Link>

            <Link to="/tickets">
              My Tickets
            </Link>

            <Link
              to="/notifications"
              className="notification-link"
            >
              Notifications

              {unreadCount > 0 && (
                <span className="notification-badge">
                  {unreadCount}
                </span>
              )}
            </Link>

            <Link to="/profile">
              Profile
            </Link>

            <span className="welcome-user">
              Hi, {user.username}
            </span>

            <button
              onClick={handleLogout}
              className="logout-button"
            >
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login">
              Login
            </Link>

            <Link to="/register">
              Register
            </Link>
          </>
        )}

      </div>

    </nav>
  );
}

export default Navbar;