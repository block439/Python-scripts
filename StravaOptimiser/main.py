import requests
from decouple import config

# creating request to get access token to our API on Strava
url = "https://www.strava.com/oauth/token"
data = {
    'client_id': config('client_id', default=" "),
    'client_secret': config('client_secret', default=" "),
    'refresh_token': config('refresh_token', default=" "),
    'grant_type': "refresh_token",
    'f': "json"
}
res = requests.post(url, data=data)
access_token = res.json()['access_token']

# getting all activities
activities_url = "https://www.strava.com/api/v3/athlete/activities"
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 5, 'page': 1}
res = requests.get(activities_url, headers=header, params=param).json()

# searching for no-swag rides below 10km and hiding it
for _ in res:
    if (_['distance']/1000) < 10:
        if 'Python_optimised' not in _['name']:
            _['name'] += '. Python_optimised'
            _['commute'] = 'true'
            _['private'] = 'true'
            _['visibility'] = 'only_me'
            url3 = f"https://www.strava.com/api/v3/activities/{_['id']}"
            res = requests.put(url3, headers=header, data=_)
        else: continue




