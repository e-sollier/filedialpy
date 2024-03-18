import sys
import shutil


if sys.platform=="linux":
    zenity_path = shutil.which("zenity")
    if zenity_path is not None: from filedialpy.linux_zenity import *
    else:
        kdialog_path=shutil.which("kdialog")
        if kdialog_path is not None: from filedialpy.linux_kdialog import *
        else: 
            # use tkinter filedialogs if neither zenity nor kdialog are available.
            from filedialpy.linux_tkinter import *
elif sys.platform=="win32":
    from filedialpy.windows import *
else:
    from filedialpy.mac import *