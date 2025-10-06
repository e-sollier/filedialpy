import os
import win32gui
import win32con
from win32com.shell import shell, shellcon


def windows_wrapper(initial_dir=None,initial_file=None,filter=None,title=None,multiple=False,directory=False,save=False,confirm_overwrite=True):
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

    if save and confirm_overwrite:
        if "Flags" in kwargs: kwargs["Flags"] = kwargs["Flags"] | win32con.OFN_OVERWRITEPROMPT
        else:  kwargs["Flags"] = win32con.OFN_OVERWRITEPROMPT
        

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

def saveFile(initial_dir=None,initial_file=None,filter=None,title=None,confirm_overwrite=True):
    return windows_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,save=True)

def browse_callback(hwnd, uMsg, lParam, lpData):
    if uMsg == shellcon.BFFM_INITIALIZED:
        # Use BFFM_SETSELECTIONW (WM_USER + 103) for Unicode paths
        win32gui.SendMessage(hwnd, win32con.WM_USER + 103, 1, lpData)
    return 0

def openDir(initial_dir=None, title="Choose a folder", **kwargs):
    try:
        initial_dir = str(initial_dir)
        if not os.path.exists(initial_dir):
            initial_dir = None
        elif os.path.isfile(initial_dir):
            initial_dir = os.path.dirname(initial_dir)
        elif not os.path.isdir(initial_dir):
            raise AssertionError("Expected code to be unreachable")
    except Exception:
        initial_dir = None

    pidl, display_name, image_list = shell.SHBrowseForFolder(
        win32gui.GetDesktopWindow(),  # Parent window
        None,  # Root PIDL (None for desktop, allowing full browsing)
        "Select a folder",  # Dialog title
        0x40,  # Optional: Modern dialog style (0x40)
        browse_callback,  # Callback function
        initial_dir  # Passed as callback_data
    )
    
    if pidl is not None:
        path = shell.SHGetPathFromIDListW(pidl)
        return path
    else:
        return ""