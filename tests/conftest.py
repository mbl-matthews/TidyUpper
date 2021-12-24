import pytest
import os
import shutil

from pathlib import Path

env = "./env"
testfiles = [
    "pidiaef.pdf",
    "archive.rar",
    "archive.zip",
    "archive.7z",
    "executable.exe",
    "executable.msi"
]

def cleanup():
    shutil.rmtree(env)
    pass

@pytest.fixture(scope="session", autouse=True)
def cwd():
    os.chdir("./tests")

@pytest.fixture(scope="function", autouse=True)
def create_env(request):
    request.addfinalizer(cleanup)
    
    try:
        os.mkdir(env)
        
        with open(os.path.join(env, "settings.ini"), 'w') as f:
            content = """
[schedule]
interval=3600
modified=3600

[directory]
watch={0}

[folder]
archives={{"path":"Archives", "filetype":"rar,zip,7z"}}
pdfs={{"path":"PDFs", "filetype":"pdf"}}
exes={{"path":"EXEs", "filetype":"exe,msi"}}
isos={{"path":"ISOs", "filetype":"iso"}}
imgs={{"path":"Images", "filetype":"jpg,jpeg,gif,png"}}

[options]
sub_for_datatype=false
            """.format(os.path.join(os.getcwd(), env)).strip()
            f.write(content)
            
        for f in testfiles:
            Path(os.path.join(env, f)).touch()
            
    except FileExistsError:
        pass
