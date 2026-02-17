from datetime import datetime, timedelta  # You must import timedelta too

now = datetime.now()
print(now.strftime("%B %d, %Y")) 
future_date = now + timedelta(days=7)

print(f"Future Date: {future_date.strftime('%B %d, %Y')}")