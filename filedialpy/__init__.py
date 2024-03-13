import sys
import shutil


if sys.platform=="linux":
    zenity_path = shutil.which("zenity")
    if zenity_path is not None: from filedialpy.linux_zenity import *
    else:
        kdialog_path=shutil.which("kdialog")
        if kdialog_path is not None: from filedialpy.linux_kdialog import *
        else: raise Exception("On linux, easier zenity or kdialog must be installed in order to use filedialpy.")
elif sys.platform=="win32":
    from filedialpy.windows import *
else:
    from filedialpy.mac import *