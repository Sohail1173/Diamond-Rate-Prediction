import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="DiamondProject"

list_of_files=[
    ".github/worflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/logger/logging.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exception.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py"
   
    
    "setup.py",
    "templates/index.html"]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")