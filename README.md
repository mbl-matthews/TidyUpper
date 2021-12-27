# TidyUpper

This tool is menat to help organize directories. The development started due to the need of organizing messy directories by filetype.

This tool will create a certain structure based on what is configured in the ```config.json``` file. Including:
- multiple directories for specified file extenions
- a directory for unknown directories
- a directory for every file extension that aren't specified in the config

# Setup

Simply clone the repository. The default ```config.json``` shows an example configuration on which one can base their own.

The directory that shall be cleaned up needs to be configured under watch. You can use ```~``` to refer to your home dir.

To add a new directory with file extenions simply add a json object containing a ```path```key with with the path relative to the specified watching directory
and a ```filetypes``` array with the file extensions listed.

If you wish to automate this, i.e. with the Windows task scheduler, you can utilize the ```run.bat``` to run the script

# Options

## Subfolders for each filetype contained

The option `sub_for_datatype` expects a boolean value. If set to true the script will create in each `folder`-directory a directory for each filetype contained. These filetype-directories will contain symbolic/soft links to each file in the `folder`-directory with the given filetype.

### Execution on Windows

If the sub_for_datatype option is set to true then on Windows enviorments the script must be executed from a command line where the executing user has the right to create symbolic links. By default users do not have this option. The easists solution is to run the `run.bat` as administrator or to execute the script from a command line thats started as administrator. Command Line programs that grant you administrator permissions such as [gsudo](https://github.com/gerardog/gsudo) can be handy here.

# Tests

To test the application [tox](https://tox.wiki/en/latest/index.html) with [pytest](https://docs.pytest.org/en/6.2.x/) is used. When testing the `sub_for_datatype` option on windows `tox` must be started with administrator permissions.
