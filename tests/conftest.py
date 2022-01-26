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
    "executable.msi",
    "os.iso",
    "i.jpg",
    "i.jpeg",
    "m.gif",
    "g.png",
    "leftover.raw",
]
testfolder = [
    "extra_folder/",
]


def cleanup():
    shutil.rmtree(env)
    pass


@pytest.fixture(scope="session", autouse=True)
def cwd():
    os.chdir("./tests")
    
    if os.path.exists(env): 
        shutil.rmtree(env)
        

@pytest.fixture(scope="function", autouse=True)
def create_env(request):
    request.addfinalizer(cleanup)
    
    try:
        os.mkdir(env)
                
        with open(os.path.join(env, "config.json"), 'w') as f:
            content = """
{
    \"schedule\": {
        \"interval\": 3600,
        \"modified\": 3600
    },
    \"directory\": {
        "watch": \""""+os.path.join(os.getcwd(), "env").replace("\\", "\\\\")+"""\"
    },
    \"folder\": [
        {
            \"path\": \"Archives\",
            \"filetypes\": [
                \"rar\",
                \"zip\",
                \"7z\"
            ]
        },
        {
            \"path\": \"PDFs\",
            \"filetypes\": [
                \"pdf\"
            ]
        },
        {
            \"path\": \"EXEs\",
            \"filetypes\": [
                \"exe\",
                \"msi\"
            ]
        },
        {
            \"path\": \"ISOs\",
            \"filetypes\": [
                \"iso\"
            ]
        },
        {
            \"path\": \"Images\",
            \"filetypes\": [
                \"jpg\",
                \"jpeg\",
                \"gif\",
                \"png\"
            ]
        }
    ],
    \"options\": {
        \"sub_for_datatype\": true
    }
}
            """.strip()
            print(content)
            f.write(content)
            
        for f in testfiles:
            Path(os.path.join(env, f)).touch()
            
        for d in testfolder:
            os.mkdir(os.path.join(env, d))
            
    except FileExistsError:
        pass

