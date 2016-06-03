import requests
import time
import json
from pprint import pprint
from config_file_stamates import *

# city = '4508722'
# api_key = WEATHER_API_KEY
# url = 'http://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&id=' + city
# # submit post request
# r = requests.get(url).json()
# display the response to screen

# import pdb; pdb.set_trace()

with open('test_result.json') as data_file:
    r = json.load(data_file)
    print r['city']['name'] + " temperatures:"
    for data in r['list']:
        temp = data['main']['temp'] * 9.0/5.0 - 459.67
        if temp > 80:
            shorts = ' (wear some shorts)'
        else:
            shorts = ''
        print time.strftime('%a (%m/%d) at %I %p - ', time.localtime(data['dt'])) + " is " + str(temp) + shorts

# with open("test_result.json", "wb") as code:
#     code.write(r.content)
