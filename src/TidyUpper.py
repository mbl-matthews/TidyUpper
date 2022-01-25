import os
import configparser
import json
import pathlib

from src.tidy import Tidy
from src.subdir import Subdir

def run(options={"config": "config.json"}):

    f = open(options["config"])
    config = json.load(f)

    watch = config["directory"]["watch"]
    if watch[0] == "~":
        home = str(pathlib.Path.home())
        watch = home+watch[1:]
    watch = watch.replace("\\", "/")
    if watch[-1] != "/":
        watch = watch + "/"

    folders = {
        "extra": {
            "path": os.path.join(watch, "Extra/"),
            "reg": None
        },
        "leftover": {
            "path": os.path.join(watch, "Leftover/"),
            "reg": None
        },
    }
    
    Tidy.sort(config, folders, watch)
    Subdir.link(config, folders, watch)              
                    
if __name__ == "__main__":
    print("Running whole TidyUpper Script")
    run()
