import os, time

from django.shortcuts import render_to_response

def listing(request, path):
    base = "/var/"

    allfiles = os.listdir(base + path)
    files = []
    dirs = []
    for i in allfiles:
        fullpath = base + path + "/" + i
        print fullpath
        if(os.path.isfile(fullpath)):
            files.append( { "name": i, "size": os.path.getsize(fullpath), "mtime": time.ctime(os.path.getmtime(fullpath))  } )
        elif(os.path.isdir(fullpath)):
            dirs.append( { "name": i, "size": os.path.getsize(fullpath), "mtime": time.ctime(os.path.getmtime(fullpath))  } )
      
    return render_to_response('listing.html', {'directory': base + path, 'file_list': files, 'dir_list': dirs, 'path': path })
