import os
from pathlib import Path

package_name = "APS-Fault-Prediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_training.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh"
]

# Here we will create the directories

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    """
    How exists_ok works: if "directory" already exists,
    os.makedirs() will not raise an exception, and it will not try to create a directory.
    If directory doesn't exist then it will create it. 
    """

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # File is missing or empty
        with open(filepath,"w") as f:
            pass
    else:
        print("File already exists")