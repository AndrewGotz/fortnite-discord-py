import requests
import json


def apiLoad(name, console):
    headers = {
        'TRN-Api-Key': 'fakeToken'
    }
    r = requests.get('https://api.fortnitetracker.com/v1/profile/' + console + '/' + name, headers=headers)
    text = json.loads(r.text)
    return text

def totalWins(name, console):
    apiJson = apiLoad(name, console)
    if 'lifeTimeStats' in apiJson:
        return str(apiJson['lifeTimeStats'][8]['value'])
    return '0'


