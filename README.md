# filedialpy

Python package for opening native file dialogs on linux, macOS and windows. It uses either zenity or kdialog on linux, pywin32 on windows and applescript on macOS.

## Installation

```
pip install filedialpy
```

## Usage

```
import filedialpy

f=filedialpy.openFile()    # Open a single file (return a string)
f=filedialpy.openFiles()   # Open multiple files (return a list of strings)
f=filedialpy.openDir()     # Open a directory (return a string)
f=filedialpy.saveFile()    # Save to a new file (return a string)

# Using additional options
f=filedialpy.saveFile(initial_dir="/home/user/Documents",initial_file="config.json",title="Save config file", filter=["*.json","*"])
```

## Options

- **initial_dir**: Initial directory where to start the search (current working directory if not specified).
- **initial_file**: Initial filename.
- **title**: Title for the dialog window.
- **filter**: string "*.json *.txt" (different accepted extensions can be separated by a space), or a list of such strings in order to provide several possible filters.


## Acknowledgements
The implementation of filedialpy was inspired by [crossfiledialog](https://github.com/maikelwever/crossfiledialog).
