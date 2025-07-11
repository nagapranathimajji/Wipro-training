#datetime
from datetime import datetime
now=datetime.now()
#datetime.now() returns the current local date and time.
print("current local date and time:",datetime.now())

#datetime.strptime() converts a string to a datetime object. strptime = string parse time
print("(str to obj conversion)strptime:",datetime.strptime("2023-10-01 12:30:45", "%Y-%m-%d %H:%M:%S"))

#epoch time
#epoch time is the number of seconds since January 1, 1970, 00:00:00 (UTC).
print("epoch time:",datetime.fromtimestamp(0))  # January 1, 1970, 00:00:00 UTC

#datetime.strftime() formats a datetime object as a string. strftime = string format time
print("(formats a datetime object as a string.) strftime() :",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
formatted=now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted)
formatted_date=now.strftime("%d-%m-%y %H:%M:%S")
print("Formatted date and time:", formatted_date)

#timedelta
from datetime import timedelta  
#timedelta represents a duration, the difference between two dates or times.
#timedelta(days=1) represents a duration of one day.
print("timedelta tommorow:",now + timedelta(days=1))  # Current date and time plus one day
print("timedelta yesterday:",now - timedelta(days=1)) 
print("timedelta future time after 3 and half hours:",now + timedelta(hours=3, minutes=30))  # Current date and time plus 3.5 hours
ftime=now + timedelta(hours=3, minutes=30)
#date.today()
from datetime import date
#date.today() returns the current local date.
print("current local date:",date.today())

#12hour and 24 hour format
#strftime() formats a datetime object as a string.
print("12 hour format:",ftime.strftime("%I:%M %p"))  # 12-hour format with AM/PM
print("24 hour format:",ftime.strftime("%H:%M %p"))  # 24-hour format

