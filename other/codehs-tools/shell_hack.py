from subprocess import run
from os import getcwd

USERNAME = "usrname"

while True:
    run(input(f"{USERNAME}@codehs:{getcwd() if getcwd() else '~'} $ "), shell=True)