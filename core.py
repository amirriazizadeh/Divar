# core.py
from datetime import datetime


class Event:
    def __init__(self, name: str, date: str, capacity: int, description: str = ""):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.description = description

    def __str__(self):
        return (
            f"Event(name='{self.name}', date='{self.date}', "
            f"capacity={self.capacity}, remaining={self.remaining_capacity}, "
            f"description='{self.description}')"
        )


class User:
    def __init__(self, username: str, password: str, national_id: str):
        self.username = username
        self.password = password
        self.national_id = national_id

    def __str__(self):
        return f"User(username='{self.username}', national_id='{self.national_id}')"


class Ticket:
    def __init__(self, user: User, event: Event):
        self.user = user
        self.event = event
        self.issued_at = datetime.now()

    def __str__(self):
        return (
            f"Ticket(user={self.user.username}, event={self.event.name}, issued_at='{self.issued_at}')"
        )


class Auth:
    _instance = None
    _admin_username = "admin"
    _admin_password = "admin123"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Auth, cls).__new__(cls)
            cls._instance._users = {}
            cls._instance._tickets = []
            cls._instance._events = []
            cls._instance._is_authenticated = False
        return cls._instance

    def login_admin(self, username: str, password: str) -> bool:
        if username == self._admin_username and password == self._admin_password:
            self._is_authenticated = True
            print("Admin authenticated successfully.")
            return True
        else:
            print("Invalid admin credentials.")
            return False

    def logout_admin(self):
        self._is_authenticated = False
        print("Admin logged out.")

    def register(self, username: str, password: str, national_id: str) -> bool:
        if not self._is_authenticated:
            print("Admin authentication required.")
            return False

        if username in self._users:
            print("Username already exists.")
            return False

        self._users[username] = User(username, password, national_id)
        print("User registered successfully.")
        return True

    def get_registered_users(self) -> list:
        return list(self._users.values())

    def get_user(self, username: str) -> User or None:
        return self._users.get(username)

    def add_event(self, name: str, date: str, capacity: int, description: str = "") -> Event or None:
        if not self._is_authenticated:
            print("Admin authentication required.")
            return None

        for event in self._events:
            if event.name == name:
                print("Event with this name already exists.")
                return None

        event = Event(name, date, capacity, description)
        self._events.append(event)
        print("Event added successfully.")
        return event

    def get_all_events(self) -> list:
        return self._events

    def issue_ticket(self, username: str, event_name: str) -> Ticket or None:
        user = self.get_user(username)
        if user is None:
            print("User not found.")
            return None

        event = self._find_event_by_name(event_name)
        if event is None:
            print("Event not found.")
            return None

        if event.remaining_capacity <= 0:
            print("Event is full. No tickets available.")
            return None

        for ticket in self._tickets:
            if ticket.user.username == username and ticket.event.name == event.name:
                print("User already has a ticket for this event.")
                return None

        ticket = Ticket(user, event)
        event.remaining_capacity -= 1
        self._tickets.append(ticket)
        print("Ticket issued successfully.")
        return ticket

    def cancel_ticket(self, username: str, event_name: str) -> bool:
        for ticket in self._tickets:
            if ticket.user.username == username and ticket.event.name == event_name:
                self._tickets.remove(ticket)
                ticket.event.remaining_capacity += 1
                print("Ticket canceled successfully.")
                return True
        print("Ticket not found.")
        return False

    def get_tickets_for_user(self, username: str) -> list:
        return [t for t in self._tickets if t.user.username == username]

    def get_all_tickets(self) -> list:
        return self._tickets

    def get_participant_count_for_event(self, event_name: str) -> int:
        return sum(1 for t in self._tickets if t.event.name == event_name)

    def _find_event_by_name(self, name: str) -> Event or None:
        for event in self._events:
            if event.name == name:
                return event
        return None

# a = Auth()
# a.login_admin("admin","admin123")