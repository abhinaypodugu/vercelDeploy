import sys
import click
import os
import importlib
import inspect
from vercelDeploy.lambdaService import LambdaService
import shutil
from pip._internal.operations import freeze

#create requirements.txt file
def createRequirements():
    x = freeze.freeze()

    with open("build\\requirements.txt", "w") as file1:
        # Writing data to a file
        for p in x:
            file1.write(p + '\n')
        
#create vercel.json file 
def createVercelJSON():
    vercel_json = """{
        "builds": [
            {"src": "/fast_api.py", "use": "@vercel/python"}
        ],
        "routes": [
            {"src": "/(.*)", "dest": "/fast_api.py"}
        ]
    }"""

    with open("build\\vercel.json", "w") as file1:
        file1.write(vercel_json)

# ----------------------- Interface -----------------------
@click.group()
@click.version_option("1.0.0")
def vercelDeploy_cli():
    print("VercelDeploy Command Line Interface")

# ---------------------- Build Code -----------------------------------
@vercelDeploy_cli.command(
    help="Build module using path and save it",
)
@click.option(
    '--path',
    type=click.STRING,
    default=".",
    help='The path to .py file'
)
def build(path):    
    if path[-2:] != "py":
        raise Exception("Given file is not a valid python file")

    head, module_name = os.getcwd(), path
    sys.path.append(head)
    module_name = module_name[:-3]
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        raise Exception(f"Could not import module:", e)

    classObj = None

    for _, obj in inspect.getmembers(module):
        try:
            if inspect.isclass(obj) and issubclass(obj, LambdaService):
                classObj = obj
        except:
            pass
    # Try to get the files under the build folder
    try:
        #Copy all source files into build folder
        root_dir = os.getcwd()
        temp_dir = root_dir + r'\build'

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

        try:
            os.mkdir(temp_dir)
        except Exception as e:
            os.rmdir(temp_dir)

        # Get all the files in the root directory inside the build folder except the __pycache__ and the build folder itself
        for files in os.listdir(root_dir):
            try:
                if(os.path.isdir(os.path.join(root_dir, files)) and files != "__pycache__" and files != "build"):
                    shutil.copytree(files, os.path.join(temp_dir, files), dirs_exist_ok= False)

                elif( files != "__pycache__" and files != "build"):
                    shutil.copy(files, temp_dir)
            except Exception as e:
                print(e)

        # Create the fast_api file from the template.py 
        LambdaService.create_fastapi_file(classObj, module_name)
        
        #create requirements.txt
        createRequirements()

        #create vercel.json
        createVercelJSON()

    # Raise exception if something went wrong in generating the build folder
    except Exception as e:
        print(f"{e} \nUnable to save the files.")

    print("All necessary modules saved.")
    return vercelDeploy_cli

# ------------------------------- Deploy -----------------------------------
@vercelDeploy_cli.command(
    help="Deploy the Lambda functions onto the vercel",
)
def deploy():
    if not os.path.exists('build'):
        print('Build the project before trying to deploy it.')
        return
    os.system('vercel build')
