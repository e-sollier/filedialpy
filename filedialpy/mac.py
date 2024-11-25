import os

import subprocess

def mac_wrapper(initial_dir=None,initial_file=None,filter=None,
             title=None,multiple=False,save=False,directory=False):
    if directory: cmd="choose folder"
    else: cmd = "choose file"
    if save: 
        cmd+= " name"
        if initial_file is not None:
            cmd+=" default name \""+initial_file+"\""
    if initial_dir is not None:
        cmd+=" default location \""+initial_dir+"\""
    if title is not None:
        cmd+=" with prompt \""+title+"\""
    if filter is not None:
        filter=filter.split(" ")
        filter = [x.lstrip("*.") for x in filter]
        filter_string=",".join("\""+fi+"\"" for fi in filter)
        cmd+=" of type {"+filter_string+"}"
    if multiple: cmd+=" with multiple selections allowed"
    #res=subprocess.run(["osascript","-"],input="the POSIX path of ("+cmd+")",text=True, capture_output=True)
    res=subprocess.run(["osascript","-"],input=cmd,text=True, capture_output=True)
    res=res.stdout.strip().split(",")
    res=[x[x.find(":"):].replace(":","/") for x in res]
    if not multiple: res=res[0]
    return res

def openFile(initial_dir=None,initial_file=None,filter=None,title=None):
    return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                filter=filter,title=title)
    
def openFiles(initial_dir=None,initial_file=None,filter=None,title=None):
    return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                filter=filter,title=title,multiple=True)
    
def openDir(initial_dir=None,initial_file=None,filter=None,title=None):
    return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                filter=filter,title=title,directory=True)

def openDirs(initial_dir=None,initial_file=None,filter=None,title=None):
    return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                filter=filter,title=title,directory=True,multiple=True)
    
def saveFile(initial_dir=None,initial_file=None,filter=None,title=None,confirm_overwrite=True):
    try:
        return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                filter=filter,title=title,save=True)
    except: # "of type " not working for "choose file name"
        return mac_wrapper(initial_dir=initial_dir,initial_file=initial_file,
                title=title,save=True)