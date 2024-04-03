import requests


with open('config.json', 'r') as file:
    data = json.load(file)
    
# ALERT: This is intended for Unifier Discord Bot, and it adapts to its behaviors.
API_KEY = data["WATCHTOWER_API_KEY"]

# DO NOT CHANGE THIS IF YOU DONT KNOW WHAT YOU ARE DOING:
WATCHTOWER_NODE = "https://watchtower.altex.page"

# STATS: ok, wrong_apikey, unexpected_error

def report_user_warned(user, mod, reason):
    global API_KEY
    global WATCHTOWER_NODE
    req = requests.get(f"{WATCHTOWER_NODE}/unifier/warn/{API_KEY}/{user}/{mod}/{reason}")
    resp = req.text
    if resp == "ok":
        return True
    else:
        return False


def report_user_gban(user, mod, reason, duration):
    global API_KEY
    global WATCHTOWER_NODE
    req = requests.get(f"{WATCHTOWER_NODE}/unifier/gban/{API_KEY}/{user}/{mod}/{duration}/{reason}")
    resp = req.text
    if resp == "ok":
        return True
    else:
        return False
