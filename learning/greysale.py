from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import threading

headless = "e"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
PATH = "C:\Program Files (x86)\chromedriver.exe"

fn = []
ln = []
nv = []

def stopwatch():
    sec = 0
    min = 0
    global etime
    while True:
        etime = f"[{min}:{'0' if sec < 10 else ''}{str(sec)}]"
        time.sleep(1)
        sec += 1
        if sec == 60:
            sec = 0
            min += 1

def listgen(flist, ntype):
    while len(flist) != 20:
        ni = input(f"{etime} Enter {ntype} name varient #{len(flist) + 1}: ")
        if len(ni.strip(""" `"1234567890-=~!@#$%^&*()_+[]\{}|;,./<>: """)) <= 1:
            terminal("Your input must be greater than one character. ")
        else:
            for x in flist:
                if ni.lower() == x.lower():
                    terminal(f"Do not repeat {ntype} name varients. ")
                    break
            else:
                flist.append(ni)
threading.Thread(target=stopwatch).start()

def terminal(content):
    print(etime, content)

terminal("Path located")

while headless[0].lower() != "y" and headless[0].lower() != "n":
    headless = input(f"{etime} Would you like to run chrome in headless mode (y/n)?: ")
    if headless[0].lower() == "y":
        driver = webdriver.Chrome(PATH, chrome_options=options)
    elif headless[0].lower() == "n":
        driver = webdriver.Chrome(PATH)
    else:
        terminal("Please enter a valid response.")

terminal("Chrome web driver initialized")
link = input(f"{etime} Paste the link of the desired lottery (format should be https://lottery.broadwaydirect.com/show/...): ")
driver.get(link)

listgen(fn, "first")
listgen(ln, "last")

for x in fn:
    for y in ln:
        nv.append(f"{x} {y}")
        terminal(f"Created name #{len(nv)}: {x} {y}")


quit()
