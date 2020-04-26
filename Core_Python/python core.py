# in this code contains
                #format
                #date and time
                

# format in python

op = "Hello, {0} {1}".format("Rohan", "kumara")
print(op)
print(f'Hello, {"Rohan"} {"Kumara"}')
print(f'Fuck off python {"Rohan"}')

# date
from datetime import datetime

#current date & time
today = datetime.now()
# this functions return a datetime object
print(f'Today is: {str(today)}')

# timedelta is used to define a period of time
from datetime import timedelta

one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday was: {str(yesterday)}')

# print date month year separetly 
