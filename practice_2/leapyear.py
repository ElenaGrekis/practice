#!/usr/bin/python

def isLeapYear( y ):
    if(not(y % 400) or ((y % 100) and not(y & 3))):
        return True
    else:
        return False

try:
    year = int(raw_input('Enter year: '))
    if(year > 0 and year < 9999):
        if(isLeapYear(year)):
            print "Cool the " + str(year) + " year is leap!"
        else:
            print str(year) + " not leap year"
except (ValueError, TypeError):
    print "Error in year! Try again"
