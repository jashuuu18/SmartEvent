import { useEffect, useState } from "react";
import { toast } from "react-toastify";

import api from "../services/api";
import EventCard from "../components/EventCard";

function Home() {
  const [events, setEvents] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(true);

  const fetchEvents = async () => {
    try {
      setLoading(true);

      const response = await api.get("/events/", {
        params: {
          search: search || undefined,
          category: category || undefined,
        },
      });

      setEvents(response.data);
    } catch (error) {
      console.error("Error loading events:", error);

      toast.error(
        error.response?.data?.detail ||
        "Unable to load events"
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, [category]);

  const handleSearch = (event) => {
    event.preventDefault();
    fetchEvents();
  };

  return (
    <div className="home-page">

      {/* Hero Section */}
      <section className="hero-section">
        <h1>
          Discover Amazing Events
        </h1>

        <p>
          Find exciting events and book your tickets
          easily with SmartEvent.
        </p>
      </section>

      {/* Search Section */}
      <section className="event-search-section">

        <form
          onSubmit={handleSearch}
          className="search-form"
        >
          <input
            type="text"
            placeholder="Search events..."
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
          />

          <select
            value={category}
            onChange={(event) =>
              setCategory(event.target.value)
            }
          >
            <option value="">
              All Categories
            </option>

            <option value="Music">
              Music
            </option>

            <option value="Tech">
              Tech
            </option>

            <option value="Sports">
              Sports
            </option>

            <option value="Business">
              Business
            </option>
          </select>

          <button type="submit">
            Search
          </button>
        </form>

      </section>

      {/* Events */}
      <section className="events-section">

        <h2>
          Upcoming Events
        </h2>

        {loading ? (
          <p className="loading-message">
            Loading events...
          </p>
        ) : events.length === 0 ? (
          <p className="no-events">
            No events found.
          </p>
        ) : (
          <div className="events-grid">
            {events.map((event) => (
              <EventCard
                key={event.id}
                event={event}
              />
            ))}
          </div>
        )}

      </section>

    </div>
  );
}

export default Home;