import requests
from pprint import pprint

headers = {
    'X-Authentication-Token': '9SbQcSRVXSyuOJdv4yeXigtt',
}

params = (
    ('name', 'Aloe'),
)
data = requests.get('https://api.speciesplus.net/api/v1/taxon_concepts.json?name=Aloe', headers=headers)
a_data=data.text
pprint(a_data)
