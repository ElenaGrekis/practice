#!/usr/bin/python

import os.path


fname = raw_input('Enter filename to read: ')
if(os.path.isfile(fname)):
    fopen = open(fname)

    _list=[]
    for line in fopen.readlines():
        _list.append(tuple(line.split()))
    fopen.close()

    for item in _list:
        print item[0] + " " + item[1]
    if(os.path.isfile(fname)):
        fopen = open(fname, 'w')
        for item in _list:
            fopen.writelines(item[0] + ' ' + item[1]+ '\n')

        fopen.writelines(raw_input('Enter new host: '))
        fopen.close()
    else:
        print "File NOT FOUND!!!"
else:
    print "File NOT FOUND!!!"
