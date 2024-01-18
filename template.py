import os
from pathlib import Path
import logging

logging.basicConfig( level= logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_of_files = [                     # .gitkeep will help to Store or save EMPTY FOLDERS
    ".github/workflows/.gitkeep",      # .github is for deployment , when we commit, It will automatically deploy in the cloud
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",     ## Build the Docker Image of the Source Code and will Deploy
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)   # Tells it is a WindowPath or LinuxPath
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True )
        logging.info(f"Creating Directory:{filedir} for the file {filename}")

    if ( not os.path.exists( filename)) or (os.path.getsize(filename) == 0 ):
        with open( filepath , 'w') as f:
            pass
            logging.info(f"Creating Empty File: {filename}")
    else:
        logging.info(f"The File: {filename} already exist")





