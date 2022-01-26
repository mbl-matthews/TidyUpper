from multiprocessing.sharedctypes import Value
import os
import configparser
import json
import pathlib

from src.tidy import Tidy
from src.subdir import Subdir

def run(options={"config": "config.json"}, preloaded_config=None):

    config = None
    if preloaded_config is None:
        f = open(options["config"])
        config = json.load(f)
    else:
        config = preloaded_config
        
    if config is None:
        raise ValueError("No config has been loaded.")

    watch = config["directory"]["watch"]
    if watch[0] == "~":
        home = str(pathlib.Path.home())
        watch = home+watch[1:]
    watch = pathlib.Path(watch)

    options = {}
    options["disable_extra"] = False
    if "options" in config and "disable_extra" in config["options"]:
        options["disable_extra"] = config["options"]["disable_extra"]
        
    options["disable_leftover"] = False
    if "options" in config and "disable_leftover" in config["options"]:
        options["disable_leftover"] = config["options"]["disable_leftover"]

    folders = {}
    if not options["disable_extra"]:
        folders["extra"] = {
            "path": watch / "Extra/",
            "reg": None
        }
        
    if not options["disable_leftover"]:
        folders["leftover"] = {
            "path": watch / "Leftover/",
            "reg": None
        }
    
    Tidy.sort(config, folders, watch, options)
    Subdir.link(config, folders, watch)              
                    
if __name__ == "__main__":
    print("Running whole TidyUpper Script")
    run()
