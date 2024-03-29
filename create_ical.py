from icalendar import Calendar, Event
from datetime import datetime, timedelta
from dateutil.rrule import rrule, WEEKLY, MO

# Create a calendar
cal = Calendar()

# Create an event
event = Event()
event.add('summary', '燃やすごみ')

# Start on a Monday
start_date = datetime(2024, 3, 26)
event.add('dtstart', start_date)

# End date is the next day (Tuesday)
end_date = start_date + timedelta(days=1)
event.add('dtend', end_date)

event.add('dtstamp', datetime.now())

# The event is all-day if dtstart and dtend are dates
event['dtstart'].to_ical = lambda: b'20240326'
event['dtend'].to_ical = lambda: b'20240327'  # The next day

# Add a recurrence rule for weekly on Monday and Thursday
event.add('rrule', {'freq': 'weekly', 'byday': ['mo', 'th']})

# Exclude New Year holidays
for day in range(1, 4):
    event.add('exdate', datetime(2024, 1, day))

# Add the event to the calendar
cal.add_component(event)

# Write the calendar to a file
with open('garbage_collection.ics', 'wb') as f:
    f.write(cal.to_ical())