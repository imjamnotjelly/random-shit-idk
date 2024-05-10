import requests

url = "https://www.duolingo.com/2017-06-30/users?fields=id"
payload = {
    "age": "69",
    "distinctId": "363431f7-5e2b-4fc0-bfdf-959aff394c5e",
    "email": "storypicsedu@gmail.com",
    "fromLanguage": "en",
    "identifier": "",
    "initialReferrer": "https://www.google.com/",
    "landingUrl": "https://www.duolingo.com/settings/sound",
    "lastReferrer": "",
    "name": "dossed",
    "password": "aaaaaa",
    "signal": {
        "siteKey": "6LcLOdsjAAAAAFfwGusLLnnn492SOGhsCh-uEAvI"
    },
    "timezone": "America/New_York",
    "username": None
}


iteration = 0
while True:
    iteration += 1
    response = requests.post(url, json=payload)
    print(response.content.decode())
    if response.status_code == 200:
        print('yayyyyy')
        print('spammed:', iteration)
    else:
        print('nayyyyy')
        print(response.status_code)
        raise Exception("you goofed")