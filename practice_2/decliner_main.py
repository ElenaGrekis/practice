#!/usr/bin/python
# -*- coding: utf-8 -*-
from decliner import humanizer

try:
    hour = raw_input('Enter hour: ')

except (ValueError, TypeError):
    print "Error in input"

print humanizer(hour,  dictionary)
