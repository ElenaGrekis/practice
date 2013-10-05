#!/usr/bin/python

def isLeapYear(y):
    return (not(y % 400) or ((y % 100) and not(y & 3)))

try:
    year = int(raw_input('Enter year: '))
    if(year > 0 and year < 9999):
        if(isLeapYear(year)):
            print "Cool the year is leap!"
        else:
            print ":( not leap year"
except (ValueError, TypeError):
    print "Error in year! Try again"
