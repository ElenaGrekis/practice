#!/usr/bin/python

userInput = raw_input

months = { "january":1, "february":2, "march":3, "april":4, "may":5,
            "june":6, "july":7, "august":8, "september":9, "october":10,
           "november":11, "december":12 }

month = userInput("Enter month: ").lower()
if(months.has_key(month)):
    print "Your month number is: " + str(months[month])
else:
    print "Ahh, you type write wrong month name"

