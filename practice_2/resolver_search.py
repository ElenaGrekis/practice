#!/usr/bin/python

import os.path


fname = raw_input('Enter filename to search host: ')
if(os.path.isfile(fname)):
    fopen = open(fname)
    _list = []
    for line in fopen.readlines():
        linetest = line.split()
        _dict = {}
        _dict[linetest[0]] = linetest[1]
        _list.append(_dict)
    fopen.close()

    flag = False
    if  (raw_input('Enter \'i\' for search search by IP,\n anything else - to search by hostname: ') == 'i'):
        string = raw_input('Enter IP: ')
        for item in _list:
            if  item.has_key(string):
                flag = True
                print "Hostname FOUND: " + item[string]
                break
    else:
        string = raw_input('Enter hostname: ')
        for item in _list:
            for key, value in item.items():
                if  value == string:
                    flag = True
                    print "IP FOUND: " + key
                    break
    if(not flag):
        print "Nothing found :(("
                
else:
    print "File NOT FOUND!!!"
       
    
