#!/usr/bin/python

userInput = raw_input

months = { "January":1, "February":2, "March":3, "April":4, "May":5,
            "June":6, "July":7, "August":8, "September":9, "October":10,
           "November":11, "December":12 }

month = userInput("Enter month: ")
if(months.has_key(month)):
    print "Your month number is: " + str(months[month])
else:
    print "Ahh, you type write wrong month name"

