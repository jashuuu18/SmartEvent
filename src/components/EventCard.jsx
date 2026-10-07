import { Link } from "react-router-dom";

function EventCard({ event }) {
  return (
    <div className="event-card">
      {event.banner_image ? (
        <img
          src={event.banner_image}
          alt={event.title}
          className="event-image"
        />
      ) : (
        <div className="event-image-placeholder">
          SmartEvent
        </div>
      )}

      <div className="event-card-content">
        <span className="event-category">
          {event.category}
        </span>

        <h3>{event.title}</h3>

        <p className="event-description">
          {event.description || "No description available."}
        </p>

        <p>
          📍 <strong>Location:</strong> {event.location}
        </p>

        <p>
          📅 <strong>Date:</strong>{" "}
          {new Date(event.event_date).toLocaleString()}
        </p>

        <div className="event-info">
          <span>
            ₹{event.ticket_price}
          </span>

          <span>
            {event.available_tickets} tickets left
          </span>
        </div>

        <Link
          to={`/events/${event.id}`}
          className="view-event-button"
        >
          View Details
        </Link>
      </div>
    </div>
  );
}

export default EventCard;