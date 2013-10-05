#!/usr/bin/python

userInput = raw_input

consts = {
    "M_E":        2.71828182845904523536,
    "M_LOG2E":    1.44269504088896340736,
    "M_LOG10E":   0.434294481903251827651,
    "M_LN2":      0.693147180559945309417,
    "M_LN10":     2.30258509299404568402,
    "M_PI":       3.14159265358979323846,
    "M_PI_2":     1.57079632679489661923,
    "M_PI_4":     0.785398163397448309616,
    "M_1_PI":     0.318309886183790671538,
    "M_2_PI":     0.636619772367581343076,
    "M_2_SQRTPI": 1.12837916709551257390,
    "M_SQRT2":    1.41421356237309504880,
    "M_SQRT1_2":  0.707106781186547524401
        }

print "Avaible consts are: "
print ", ".join(consts.keys())

try:
    const, perc = userInput("Input format is const:perc ").split(':')
    if(consts.has_key(const) and perc.isdigit() and perc >= 0):
        print "%.{0}f".format(perc) % consts[const]
    else:
        print "Error in input. Try again"
except (ValueError, TypeError):
    print "Bad error in input"
    
