import random
from datetime import datetime, timedelta

# Start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2030, 12, 31)

# Calculate the time difference in seconds
time_between = end_date - start_date
total_seconds = int(time_between.total_seconds())

# Generate random seconds
random_seconds = random.randint(0, total_seconds)

# Create random date and time
random_datetime = start_date + timedelta(seconds=random_seconds)

print("Random Date and Time:", random_datetime)