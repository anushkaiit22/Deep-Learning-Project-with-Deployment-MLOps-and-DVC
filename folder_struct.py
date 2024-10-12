import os 
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s] : %(message)s:')

project_name = 'Disease_Classifier'

li = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in li :
    path = Path(filepath)
    directory , name = os.path.split(path)

    if directory != "":
        os.makedirs(directory, exist_ok= True)
        logging.info(f"Creating directory;{directory}for the file :{name}")

    if(not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path,"w") as f:
            pass
            logging.info(f"Creating empty file : {path}")


    else:
        logging.info(f"{name} is laready exists") 
                   
