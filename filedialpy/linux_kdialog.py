import subprocess
import os

def kdialog_wrapper(initial_dir=None,initial_file=None,filter=None,title=None,multiple=False,directory=False,save=False):
    cmd=["kdialog"]
    if save: cmd.append("--getsavefilename")
    elif directory: cmd.append("--getexistingdirectory")
    else: cmd.append("--getopenfilename")

    if initial_dir is None:
        initial_dir=os.getcwd()
    cmd.append(initial_dir)

    if title is not None:
        cmd.append("--title")
        cmd.append(title)

    if filter is not None:
        if isinstance(filter,str):
            filter = [filter]
        cmd.append("\""+"|".join(filter)+"\"")

    if multiple:
        cmd.append("--multiple")
    result = subprocess.run(cmd,capture_output=True, text=True)
    if multiple: return [x.strip() for x in result.stdout.split(" ")]
    else: return result.stdout.strip()

def openFile(initial_dir=None,initial_file=None,filter=None,title=None):
    return kdialog_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title)

def openFiles(initial_dir=None,initial_file=None,filter=None,title=None):
    return kdialog_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,multiple=True)

def openDir(initial_dir=None,initial_file=None,filter=None,title=None):
    return kdialog_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,directory=True)

def openDirs(initial_dir=None,initial_file=None,filter=None,title=None):
    return kdialog_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,directory=True,multiple=True)

def saveFile(initial_dir=None,initial_file=None,filter=None,title=None,confirm_overwrite=True):
    return kdialog_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,save=True)
