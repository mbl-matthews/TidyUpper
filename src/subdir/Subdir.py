import os

def link(config=None, folders=None, watch=None):
    if None in [config, folders, watch]:
        raise ValueError("Missing parameters")
    
    if not config.has_option("options", "sub_for_datatype"):
        raise ValueError("Config missing mandatory options section")
        
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