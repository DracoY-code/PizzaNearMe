import os

import pandas as pd
import requests

from dotenv import load_dotenv
load_dotenv()

# Get API key
KEY = os.getenv('API_KEY')

# Intro
print('Find a pizza place near you!!!')

# Ask for the search query
place = input('Enter the location of your choice: ')

# Get the geocoding of the place
geocode_req = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
                           params=[('key', KEY), ('address', place),])
try:
    location = geocode_req.json()['results'][0]['geometry']['location']
except:
    print('Location data not found')
    exit()

# Get the search data for pizza shops in the nearby area
search_req = requests.get(
    'https://maps.googleapis.com/maps/api/place/nearbysearch/json?',
    params=[('key', KEY), ('type', 'restaurant'),
            ('radius', '3000'), ('keyword', 'pizza'),
            ('location', f'{location["lat"]},{location["lng"]}'),]
)
try:
    # Store maps of data in a list
    data = []
    for result in search_req.json()['results']:
        data.append({
            'Name': result['name'],
            'Open': result['opening_hours']['open_now'],
            'Vicinity': result['vicinity'],
            'Location': (result['geometry']['location']['lat'],
                         result['geometry']['location']['lng']),
        })
except:
    print('Pizza shops can not be found')
    exit()

# Display data using pandas DataFrame
df = pd.DataFrame(data)
print(df)

# Outro
print('This is your data. Have a good meal!')
