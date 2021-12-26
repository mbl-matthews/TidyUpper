import os
import re

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