import os
import win32gui
import win32con
from win32com.shell import shell, shellcon


def windows_wrapper(initial_dir=None,initial_file=None,filter=None,title=None,multiple=False,directory=False,save=False):
    kwargs={}
    if initial_dir is not None: kwargs["InitialDir"] = initial_dir

    if initial_file is not None: kwargs["File"] = initial_file

    if title is not None: kwargs["Title"] = title

    if filter is not None:
        if isinstance(filter,str):
            kwargs["Filter"]= filter+"\0"+filter+"\0"
        elif isinstance(filter,list):
            filters=""
            for x in filter:
                filters+=x+"\0"+";".join(x.split(" "))+"\0"
            kwargs["Filter"]=filters
        elif isinstance(filter,dict):
            filters=""
            for x in filter:
                if isinstance(filter[x],str): filters+=x+"\0"+filter[x]+"\0"
                else: filters+=x+"\0"+";".join(filter[x])+"\0"
            kwargs["Filter"]=filters

    if multiple:
        kwargs["Flags"]=win32con.OFN_ALLOWMULTISELECT  | win32con.OFN_EXPLORER
        

    try:
        hwnd = win32gui.GetForegroundWindow()
        if save:
            res=win32gui.GetSaveFileNameW(hwndOwner=hwnd,**kwargs)[0]
        else:
            res=win32gui.GetOpenFileNameW(hwndOwner=hwnd,**kwargs)[0]
    except:
        res=""
    if multiple:
        res = res.split('\x00')
        dirname=res[0]
        if len(res)>1:
            res = [os.path.join(dirname,x) for x in res[1:]]
        else: res=[]
    return res

def openFile(initial_dir=None,initial_file=None,filter=None,title=None):
    return windows_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title)

def openFiles(initial_dir=None,initial_file=None,filter=None,title=None):
    return windows_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,multiple=True)

def saveFile(initial_dir=None,initial_file=None,filter=None,title=None):
    return windows_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,save=True)

def openDir(title="Choose a folder",**kwargs):
    hwnd = win32gui.GetForegroundWindow()
    initial_pidl = shell.SHGetFolderLocation(hwnd, shellcon.CSIDL_DESKTOP, 0, 0)
    pidl, display_name, image_list = shell.SHBrowseForFolder(hwnd,initial_pidl,title, shellcon.ASSOCF_VERIFY,None, None)
    if pidl is not None: return shell.SHGetPathFromIDListW(pidl)
    else: return ""