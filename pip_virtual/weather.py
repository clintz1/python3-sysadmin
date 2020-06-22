# Creating a Weather Script
import os
import requests
import sys


from argparse import ArgumentParser


parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('--zip', '-z', help='zip/postal code to get the weather for')
parser.add_argument('--country', '-co', default='sg', help='country zip/postal belongs to, default is "us"')
parser.add_argument('--cityname', '-cn', default='singapore', help='call by city name, default is "singapore"')


args = parser.parse_args()


api_key = os.getenv('OWM_API_KEY', 'b131d747f93b3354b4e987ae5c65249c')


if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

if args.zip:
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"
else:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={args.cityname},{args.country}&appid={api_key}"


res = requests.get(url)


if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)


print(res.json())
