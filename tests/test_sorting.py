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
    "executable.msi",
    "os.iso",
    "i.jpg",
    "i.jpeg",
    "m.gif",
    "g.png",
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
    
    archives = os.path.join(env, "Archives")
    assert os.path.exists(archives)
    assert os.path.exists(os.path.join(archives, ".7z"))
    assert os.path.exists(os.path.join(archives, ".zip"))
    assert os.path.exists(os.path.join(archives, ".rar"))
    
    pdf = os.path.join(env, "PDFs")
    assert os.path.exists(pdf)
    assert os.path.exists(os.path.join(pdf, ".pdf"))
    
    exe = os.path.join(env, "EXEs")
    assert os.path.exists(exe)
    assert os.path.exists(os.path.join(exe, ".exe"))
    assert os.path.exists(os.path.join(exe, ".msi"))
      
    iso = os.path.join(env, "ISOs")
    assert os.path.exists(iso)
    assert os.path.exists(os.path.join(iso, ".iso"))
      
    img = os.path.join(env, "Images")
    assert os.path.exists(img)
    assert os.path.exists(os.path.join(img, "jpg"))
    assert os.path.exists(os.path.join(img, "jpeg"))
    assert os.path.exists(os.path.join(img, "gif"))
    assert os.path.exists(os.path.join(img, "png"))
    
    # TODO create case to test that every possible ending is covered  
    assert os.path.exists(os.path.join(env, "Leftover"))  
    assert os.path.exists(os.path.join(env, "Extra"))  
    