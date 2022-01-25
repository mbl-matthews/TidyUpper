import os
import re
import json

from src.util import Helper

def sort(config=None, folders=None, watch=None):
    if None in [config, folders, watch]:
        raise ValueError("Missing parameters")

    if not "folder" in config:
        raise ValueError("Config missing mandatory folder section")
        
    for entry in range(len(config["folder"])):
        try:
            entryjson = config["folder"][entry]
            path = entryjson["path"]
            if path[-1] != "/":
                path = path + "/"
            filetypes = entryjson["filetypes"]
            filereg = "(.*)("
            for ftype in filetypes:
                filereg = filereg + "[.]" + ftype + "|"
            filereg = filereg[:-1] + ")"

            folders[str(entry)] = {
                "path": watch / path,
                "reg": filereg
            }
        except Exception as e:
            print("Syntax Error at entry "+str(entry)+ " ; "+str(e))

    for folder in folders.values():
        if not os.path.exists(folder["path"]):
            os.mkdir(folder["path"])

    files = os.listdir(watch)
    # Move unconfigured folders into Extra directory
    for file in files:
        if not os.path.isdir(watch / file):
            continue

        # checks if a folder is configured in the config.json
        # if not move to Extra
        known_folder = False
        for folder in folders.values():
            if Helper.are_same_file(folder["path"], watch / file):
                known_folder = True
        if not known_folder:
            new_file = Helper.prepare_new_filename(folders["extra"]["path"] / file)
            os.rename(watch / file, new_file)

    files = os.listdir(watch)
    # Move each file into it's configured folder based on the config.json
    # Unconfigured filetypes will be moved into the Leftover folder
    for file in files:
        abs_file = watch / file
        if os.path.isdir(abs_file):
            continue
        try:
            matched = False
            for folder in folders.values():
                if folder["reg"] is None:
                    continue
                if re.match(folder["reg"], file):
                    new_file = Helper.prepare_new_filename(folder["path"] / file)
                    os.rename(abs_file, new_file)
                    matched = True
                    break
            if not matched:
                new_file = Helper.prepare_new_filename(folders["leftover"]["path"] / file)
                os.rename(abs_file, new_file)
        except PermissionError:
            pass
