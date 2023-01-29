import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.environ.get("API_KEY")

df = pd.read_csv('address.csv')

addresses = df['地域']
# print(addresses[0])

# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + API_KEY
# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=東京都品川区西五反田7-22-17TOCビル12階&key=' + API_KEY
# print(requests.get(url).json())

# ret = requests.get(url).json()['results'][0]['geometry']['location']

for i, address in enumerate(addresses, 0):
  url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + API_KEY
  ret = requests.get(url).json()
  if (ret['status'] == 'OK'):
    latlng = ret['results'][0]['geometry']['location']
    df['緯度'][i] = latlng['lat']
    df['経度'][i] = latlng['lng']

df.to_csv('address_withlatlng.csv')
