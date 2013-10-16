#!/usr/bin/python
# -*- coding: utf-8 -*-

def humanizer(hour, dictionary):
    if(hour.isdigit()):
        h1 = int(hour) % 10
        h2 = int(hour) % 100

        out = ""
        if(h2 in range(11, 19)):
            out = dictionary[2]
        elif(h1 == 1):
            out = dictionary[0]
        elif(h1 > 1 and h1 < 5):
            out = dictionary[1]
        else:
            out = dictionary[2]
        return (str(hour) + " " + out)
    else:
        print "Digit error"
        return ""


dictionary = {
        0:"час",
        1:"часа",
        2:"часов"
        }

if __name__ == '__main__':
    pass
