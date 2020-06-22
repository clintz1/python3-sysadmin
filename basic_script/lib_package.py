# Utilizing Packages
from time import localtime, mktime, strftime
now = localtime()
print(now)
print(now.tm_hour)

# Building a Stopwatch Script
start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")


# Wait for user to stop timer
input("Press 'Enter' to stop timer ")


stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)


print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
