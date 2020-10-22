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

Example:
```
[folder]
videos={"paths":"Videos", "filetype":"mp4,mkv,avi,webm"}
```

If you wish to automate this, i.e. with the Windows task scheduler, you can utilize the ```run.bat``` to run the script
