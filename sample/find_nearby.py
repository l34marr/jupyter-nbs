#!/usr/bin/env python

# pipenv install googlemaps
# pipenv install python-dotenv

import os
import googlemaps
import time

GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")

gmaps = googlemaps.Client(key=GOOGLE_PLACES_API_KEY)
geocode_result = gmaps.geocode('臺北市')
# ['geometry']['location'] = {'lat': 25.0329694, 'lng': 121.5654177}
geocode_location = geocode_result[0]['geometry']['location']

gmaps_return1 = gmaps.places_nearby(location=geocode_location,radius=2500,keyword='餐廳')
results_1 = gmaps_return1['results']
next_page_token1 = gmaps_return1['next_page_token']
for result in results_1:
    print(result['name'], result['place_id'], result['vicinity'], result['geometry']['location'])
# returned results are 20 records, each record is a dict, somehow randomly

time.sleep(5)

gmaps_return2 = gmaps.places_nearby(page_token=next_page_token1)
results_2 = gmaps_return2['results']
next_page_token2 = gmaps_return2['next_page_token']
for result in results_2:
    print(result['name'], result['place_id'], result['vicinity'], result['geometry']['location'])
# gmaps.place(place_id) returns more info

time.sleep(5)

gmaps_return3 = gmaps.places_nearby(page_token=next_page_token2)
results_3 = gmaps_return3['results']
# next_page_token3 = gmaps_return3['next_page_token'] KeyError
for result in results_3:
    print(result['name'], result['place_id'], result['vicinity'], result['geometry']['location'])

