#!/usr/bin/python

import os.path

readInput = raw_input

fname = readInput('Enter filename to read: ')
if(os.path.isfile(fname)):
    fopen = open(fname)

    linesList = []
    for line in fopen.readlines():
        linesList.append(line.split())
    fopen.close()

    for item in linesList:
        print item[0] + " " + item[1]
    if(os.path.isfile(fname)):
        fopen = open(fname, 'w')
        for item in linesList:
            fopen.writelines(item[0] + ' ' + item[1]+ '\n')

        fopen.writelines(readInput('Enter new host: '))
        fopen.close()
    else:
        print "File NOT FOUND!!!"
else:
    print "File NOT FOUND!!!"
