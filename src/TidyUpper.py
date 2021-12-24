import os
import re
import configparser
import pathlib
import json

from src.util import Helper
from src.tidy import Tidy
from src.subdir import Subdir

def run(options={"settings": "settings.ini"}):
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    config = configparser.ConfigParser()
    config.read(options["settings"])

    watch = config["directory"]["watch"]
    if watch[0] == "~":
        home = str(pathlib.Path.home())
        watch = home+watch[1:]
    watch = watch.replace("\\", "/")
    if watch[-1] != "/":
        watch = watch + "/"

    folders = {
        "extra": {
            "path": watch+"Extra/",
            "reg": None
        },
        "leftover": {
            "path": watch+"Leftover/",
            "reg": None
        },
    }
    
    Tidy.sort(config, folders, watch)
    Subdir.link(config, folders, watch)              
                    
if __name__ == "__main__":
    run()