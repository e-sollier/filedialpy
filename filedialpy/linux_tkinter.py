import subprocess
import os
from tkinter import Tk
import tkinter.filedialog



def convert_filter(filter):
    if filter is None: return []
    if isinstance(filter,str): filter=[filter]
    new_filters=[]
    for x in filter:
        new_filters.append((x,x.replace("*","")))
    return new_filters

def openFile(initial_dir=None,initial_file=None,filter=None,title=None):
    root = Tk()
    root.withdraw()
    print(convert_filter(filter))
    t=tkinter.filedialog.askopenfilename(initialdir=initial_dir,initialfile=initial_file,title=title,filetypes=convert_filter(filter))
    if len(t)==0: t=""
    root.destroy()
    return t

def openFiles(initial_dir=None,initial_file=None,filter=None,title=None):
    root = Tk()
    root.withdraw()
    t=tkinter.filedialog.askopenfilenames(initialdir=initial_dir,initialfile=initial_file,title=title,filetypes=convert_filter(filter))
    if len(t)==0: t=""
    root.destroy()
    return t

def openDir(initial_dir=None,initial_file=None,filter=None,title=None):
    root = Tk()
    root.withdraw()
    t=tkinter.filedialog.askdirectory(initialdir=initial_dir,initialfile=initial_file,title=title,filetypes=convert_filter(filter))
    if len(t)==0: t=""
    root.destroy()
    return t

def saveFile(initial_dir=None,initial_file=None,filter=None,title=None,confirm_overwrite=True):
    root = Tk()
    root.withdraw()
    t=tkinter.filedialog.asksaveasfilename(initialdir=initial_dir,initialfile=initial_file,title=title,filetypes=convert_filter(filter),confirmoverwrite=confirm_overwrite)
    if len(t)==0: t=""
    root.destroy()
    return t
