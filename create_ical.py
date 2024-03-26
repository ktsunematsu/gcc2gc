from icalendar import Calendar, Event
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY, MO

# Create a calendar
cal = Calendar()

# Create an event
event = Event()
event.add('summary', 'Garbage collection')
event.add('dtstart', datetime(2024, 3, 26))  # Start on a Monday
event.add('dtend', datetime(2024, 4, 26))  # End date is exclusive
event.add('dtstamp', datetime.now())

# The event is all-day if dtstart and dtend are dates
event['dtstart'].to_ical = lambda: b'20240326
event['dtend'].to_ical = lambda: b'20240426
# Add a recurrence rule for weekly on Monday
event.add('rrule', {'freq': 'weekly', 'byday': 'mo'})

# Add the event to the calendar
cal.add_component(event)

# Write the calendar to a file
with open('garbage_collection.ics', 'wb') as f:
    f.write(cal.to_ical())