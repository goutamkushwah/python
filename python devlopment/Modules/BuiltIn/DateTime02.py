import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Current date only
today = datetime.date.today()
print("Today:", today)

# Current time only
current_time = datetime.datetime.now().time()
print("Time:", current_time)

next_week = today + datetime.timedelta(days=7)
print("Next week:", next_week)

# Subtract 30 days
last_month = today - datetime.timedelta(days=30)
print("30 days ago:", last_month)
