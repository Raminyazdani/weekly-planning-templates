from datetime import datetime, timedelta

# date time objet 22 april 2025
date = "2025-04-22"
end_date = "2025-07-18"
# convert string to datetime object
date_object = datetime.strptime(date, "%Y-%m-%d")
end_date_object = datetime.strptime(end_date, "%Y-%m-%d")
current_date = date_object

while current_date < end_date_object:
    print(current_date.strftime("%Y-%m-%d"))
    # increment the date by 1 day
    current_date = current_date + timedelta(days=14)
