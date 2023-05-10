from subprocess import run
from importlib import import_module
from types import ModuleType

def install_lib(libname: str) -> ModuleType:
    run(f"python3 -m pip install {libname}", shell=True)
    return import_module(libname)
