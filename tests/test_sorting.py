import pytest
import os

from pathlib import Path
from src import TidyUpper

env = "env"
testfiles = [
    "pidiaef.pdf",
    "archive.rar",
    "archive.zip",
    "archive.7z",
    "executable.exe",
    "executable.msi"
]

def test_run():
    wd = os.getcwd()
    assert os.path.exists(env)
    
    p1 = os.path.join(Path().absolute().resolve(), env)
    p2 = os.path.join(p1, "settings.ini")
    TidyUpper.run(
        {"settings": p2}
    )
    os.chdir(wd)
    
    for f in testfiles:
        assert not os.path.exists(os.path.join(env, f))
    
    assert os.path.exists(os.path.join(env, "Archives"))  
    assert os.path.exists(os.path.join(env, "PDFs"))  
    assert os.path.exists(os.path.join(env, "EXEs"))  
    assert os.path.exists(os.path.join(env, "ISOs"))  
    assert os.path.exists(os.path.join(env, "Images"))  
    assert os.path.exists(os.path.join(env, "Leftover"))  
    assert os.path.exists(os.path.join(env, "Extra"))  
    