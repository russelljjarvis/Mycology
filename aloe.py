import os
#security token will need updating
os.system('curl -i "https://api.speciesplus.net/api/v1/taxon_concepts.xml?name=Aloe" -H "X-Authentication-Token:9SbQcSRVXSyuOJdv4yeXigtt" >> aloe.xml')
os.system('cat aloe.xml')
#import json
from pprint import pprint
import untangle

with open('aloe.xml') as data_file:
    aloe_data = untangle.parse(data_file)
pprint(aloe_data)
