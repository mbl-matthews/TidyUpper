import os
import re
import configparser
import pathlib
import json


def are_same_file(file1, file2):
    try:
        absf1 = os.path.abspath(file1)
        absf2 = os.path.abspath(file2)
        return absf1 == absf2
    except:
        return False


def file_to_name_type(prep_file):
    splitted = os.path.splitext(prep_file)
    return {
        "name": splitted[0],
        "type": splitted[1]
    }


def prepare_new_filename(prep_file):
    i = 1
    fname = {
        "name": prep_file,
        "type": ""
    }
    if not os.path.isdir(prep_file):
        fname = file_to_name_type(prep_file)

    if re.match("(.*)\\([0-9]+\\)", fname["name"]):
        cop_num = re.findall("\\([0-9]+\\)", fname["name"])[0]
        i = int(cop_num[1:-1]) + 1
    new_file = fname["name"] + fname["type"]
    while True:
        if not os.path.exists(new_file):
            return new_file
        else:
            new_file = fname["name"] + "(" + str(i) + ")" + fname["type"]
            i += 1


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config = configparser.ConfigParser()
config.read("settings.ini")

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

if config.has_section("folder"):
    for entry in config["folder"]:
        try:
            entryjson = json.loads(config["folder"][entry])
            path = entryjson["path"]
            if path[-1] != "/":
                path = path + "/"
            filetypes = entryjson["filetype"].split(",")
            filereg = "(.*)("
            for ftype in filetypes:
                filereg = filereg + "[.]" + ftype + "|"
            filereg = filereg[:-1] + ")"

            folders[entry] = {
                "path": watch + path,
                "reg": filereg
            }
        except:
            print("Syntax Error at entry "+entry)

for folder in folders.values():
    if not os.path.exists(folder["path"]):
        os.mkdir(folder["path"])

files = os.listdir(watch)
for file in files:
    known_folder = False
    for folder in folders.values():
        if are_same_file(folder["path"], watch + file):
            known_folder = True
    if not known_folder and os.path.isdir(watch+file):
        new_file = prepare_new_filename(folders["extra"]["path"] + file)
        os.rename(watch+file, new_file)

files = os.listdir(watch)
for file in files:
    if re.match("(.*)[.](.*)", file) and not re.match("(.*)[.]py", file):
        abs_file = watch + file
        try:
            matched = False
            for folder in folders.values():
                if folder["reg"] is None:
                    continue
                if re.match(folder["reg"], file):
                    new_file = prepare_new_filename(folder["path"] + file)
                    os.rename(abs_file, new_file)
                    matched = True
                    break
            if not matched:
                new_file = prepare_new_filename(folders["leftover"]["path"] + file)
                os.rename(abs_file, new_file)
        except PermissionError:
            pass

if(config.has_option("options", "sub_for_datatype")):
    sub_dirs = config["options"]["sub_for_datatype"]
    if sub_dirs == "true":
        for folder in folders.values():
            files = os.listdir(folder["path"])
            files = [ e for e in files if os.path.isfile(folder["path"]+"/"+e)]
            datatypes = []
            for file in files:
                ftokens = file.split(".")
                if ftokens[0] == file:
                    continue
                datatypes.append("."+ftokens[-1])
            for type in datatypes:
                sub_folder = folder["path"]+type
                if not os.path.exists(sub_folder):
                    os.mkdir(sub_folder)
                m_files = [e for e in files if e.endswith(type)]
                for s_file in m_files:
                    original = folder["path"]+s_file
                    symlink = sub_folder+"/"+s_file
                    if not os.path.exists(symlink):
                        os.symlink(original, symlink)
            m_files = [e for e in files if len(e.split(".")) == 0]
            sub_folder = folder["path"]+"typeless"
            if not os.path.exists(sub_folder):
                os.mkdir(sub_folder)
            for s_file in m_files:
                original = folder["path"] + s_file
                symlink = sub_folder + "/" + s_file
                if not os.path.exists(symlink):
                    os.symlink(original, symlink)