import subprocess
import os

def zenity_wrapper(initial_dir=None,initial_file=None,filter=None,title=None,multiple=False,directory=False,save=False,confirm_overwrite=True):
    cmd=["zenity","--file-selection"]

    if initial_dir is None:
        initial_dir=os.getcwd()
    if initial_file is None: initial_file=""
    filename = os.path.join(initial_dir,initial_file)
    cmd.append("--filename")
    cmd.append(filename)

    if title is not None:
        cmd.append("--title")
        cmd.append(title)

    if filter is not None:
        if isinstance(filter,str):
            filter = [filter]
        for fi in filter:
            cmd.append("--file-filter")
            cmd.append(fi)

    if multiple:
        cmd.append("--multiple")
    if directory:
        cmd.append("--directory")
    if save:
        cmd.append("--save")
        if confirm_overwrite:
            cmd.append("--confirm-overwrite")
    result = subprocess.run(cmd,capture_output=True, text=True)
    if multiple: return [x.strip() for x in result.stdout.split("|")]
    else: return result.stdout.strip()

def openFile(initial_dir=None,initial_file=None,filter=None,title=None):
    return zenity_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title)

def openFiles(initial_dir=None,initial_file=None,filter=None,title=None):
    return zenity_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,multiple=True)

def openDir(initial_dir=None,initial_file=None,filter=None,title=None):
    return zenity_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,directory=True)

def openDirs(initial_dir=None,initial_file=None,filter=None,title=None):
    return zenity_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,directory=True,multiple=True)

def saveFile(initial_dir=None,initial_file=None,filter=None,title=None,confirm_overwrite=True):
    return zenity_wrapper(initial_dir=initial_dir,initial_file=initial_file,filter=filter,title=title,save=True,confirm_overwrite=confirm_overwrite)
