#!/usr/bin/python

import os.path

readInput = raw_input


fname = readInput('Enter filename to search host: ')
if(os.path.isfile(fname)):
    fopen = open(fname)
    linesList = []
    for line in fopen.readlines():
        linetest = line.split()
        dictionary = {}
        dictionary[linetest[0]] = linetest[1]
        linesList.append(dictionary)
    fopen.close()

    flag = False
    if  (readInput('Enter \'i\' for search search by IP,\n anything else - to search by hostname: ') == 'i'):
        string = readInput('Enter IP: ')
        for item in linesList:
            if  item.has_key(string):
                flag = True
                print "Hostname FOUND: " + item[string]
                break
    else:
        string = readInput('Enter hostname: ')
        for item in linesList:
            for key, value in item.items():
                if  value == string:
                    flag = True
                    print "IP FOUND: " + key
                    break
    if(not flag):
        print "Nothing found :(("
                
else:
    print "File NOT FOUND!!!"
       
    
