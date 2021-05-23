This is simple script to hide rides on Strava below 10km.
It will make your wall cleaner and your friends will be grateful for less short activities from your profile in feed.
If you want to automate it you can use Pythonista and run this script when Strava app updates new ride to your profile,
or use webhook see: https://developers.strava.com/docs/webhooks/

First you have to create an application on your Strava account and get Client_ID and rest of credential data.
See how to do it here: https://developers.strava.com/docs/getting-started/

Create your own '.env' file to store credential data for use your application
Install python-decouple: pip install python-decouple

For updating on Strava you need extra privileges (activity:write, activity:read_all),
add this two privileges at the end of URL when you will generate access token