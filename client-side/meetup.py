import json
import requests
from config_file_stamates import *


base_url = 'https://api.meetup.com' # Base API url
group_members = '/2/members' # API to get members of a specified meetup group_members
profile = '/2/profile/'
CincyPy_ID = '2647642'
apikey = MEETUP_API_KEY

# url = base_url + group_members + '?key=' + apikey + '&group_id=' + CincyPy_ID
# output = requests.get(url).json()
#
# with open('meetup_results2.json', 'wb') as data_file:
#     data_file.write(json.dumps(output, indent=4, sort_keys=True))

with open('meetup_results2.json') as data_file:
    output = json.load(data_file)

ids = []
for item in output['results']:
    ids.append(item['id'])

members = {}
for member in ids:
    url2 = base_url + profile + CincyPy_ID + '/' + str(member) + '/' + '?key=' + apikey
    output2 = requests.get(url2).json()
    try:
        members[output2['name']] = output2['answers'][0]['answer'] # Store answer to first question (use of Python)
        print [output2['member_id']], [output2['name']], output2['answers'][0]['answer']
    except:
        pass

print members
