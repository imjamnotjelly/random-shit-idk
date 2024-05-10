import requests
from bs4 import BeautifulSoup




response = requests.get("https://discord.gg/invite/fortnite")

print(response.content.decode())