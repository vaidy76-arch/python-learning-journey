from datetime import datetime, date

# Current date and time
now = datetime.now()
print(f"Right now: {now}")

# Just today's date
today = date.today()
print(f"Today's date: {today}")

# Access individual parts
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"MicroSec: {now.microsecond}")

# Formatting dates as strings
print(f"\n--- Formatted dates ---")

# ISO format (great for sorting!)
iso_format = now.strftime("%Y-%m-%d")
print(f"ISO format: {iso_format}")

# Filename-safe timestamp (no colons!)
filename_format = now.strftime("%Y-%m-%d_%H-%M-%S")
print(f"Filename-safe: {filename_format}")

# Human-readable
human_format = now.strftime("%A, %B %d, %Y at %I:%M %p")
print(f"Human-readable: {human_format}")

# Build a real CSV filename
csv_filename = f"sales_report_{filename_format}.csv"
print(f"\nGenerated filename: {csv_filename}")

# Time differences with timedelta
from datetime import timedelta

print(f"\n--- Time calculations ---")

# What's the date 30 days from now?
thirty_days = timedelta(days=30)
future_date = now + thirty_days
print(f"30 days from now: {future_date.strftime('%Y-%m-%d')}")

# What was the date 7 days ago?
week_ago = now - timedelta(days=7)
print(f"7 days ago: {week_ago.strftime('%Y-%m-%d')}")

# How many days between two dates?
new_year = datetime(2027, 1, 1)
days_until_new_year = new_year - now
print(f"Days until 2027: {days_until_new_year.days}")

# Measure how long something takes
import time
start = datetime.now()
time.sleep(2)  # Pretend we're doing work for 2 seconds
end = datetime.now()
duration = end - start
print(f"\nOperation took: {duration.total_seconds():.2f} seconds")