from datetime import datetime
# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
dt_object = datetime.fromtimestamp(timestamp)

print(dt_object)
