# TidyUpper

This is meant to be a tool that helps to organize some directory. The idea came from a messed up Downloads directory which was very slow to open, so that there was a need to organize it.

This tool will create a certain structure based on what is configured in the ```settings.ini``` file. Including:
- multiple directories for specified file extenions
- a directory for unknown directories
- a directory for every file extension that isnt specified

# Setup

Simply clone the repository. In the ```settings.ini``` are already a few directories with file extenions specified.

The directory that shall be cleaned up needs to be configured under watch. You can use ```~``` to refer to your home dir just like in Linux even on Windows.

To add a new directory with file extenions simply give a key followed with a json object containing a ```path``` value with the path relative to watching directory
and a ```filetype``` value with the file extensions comma seperated.

If you want each folder to contain a subfolder for each filetype in the directory with symlinks to each file with the corresponding filetypes simply set the option `sub_for_datatype` to true. If not simply set the option to any other value or delete the option from your `settings.ini`.

Example:
```
[folder]
videos={"paths":"Videos", "filetype":"mp4,mkv,avi,webm"}
```

If you wish to automate this, i.e. with the Windows task scheduler, you can utilize the ```run.bat``` to run the script

# Execution

If the sub_for_datatype option is set to true then on Windows enviorments the script must be executed from a command line where the executing user has the right to create symbolic links. By default users do not have this option. The easists solution is to run the `run.bat` as administrator or to execute the script from a command line thats started as administrator.
