import requests
from pprint import pprint

#The authentication token needs refreshing every month or so.
headers = {
    
    'X-Authentication-Token': '9SbQcSRVXSyuOJdv4yeXigtt',
}

params = (
    ('name', 'Aloe'),
)
data=[]

data.append(requests.get('https://api.speciesplus.net/api/v1/taxon_concepts.json?name=Aloe', headers=headers))
identification = data[0].json()['taxon_concepts'][0]['id']
print(identification)
exec_str=str("data.append(requests.get(")
print(exec_str)

#Replace string formatting with more explicit formatting.
exec_str2=str("'https://api.speciesplus.net/api/v1/taxon_concepts.json/:")+str(identification)+str("/distributions',headers=headers))")
print(exec_str2)
exec(exec_str+exec_str2)
exec_str2=str("'https://api.speciesplus.net/api/v1/taxon_concepts.json/:")+str(identification)+str("/references',headers=headers))")
exec(exec_str+exec_str2)
exec_str2=str("'https://api.speciesplus.net/api/v1/taxon_concepts.json/:")+str(identification)+str("/eu_legislation',headers=headers))")
exec(exec_str+exec_str2)
exec_str2=str("'https://api.speciesplus.net/api/v1/taxon_concepts.json/:")+str(identification)+str("/cites_legislation',headers=headers))")
exec(exec_str+exec_str2)

print(len(data))
for i in data:
    print(i)
    if '<Response [200]>' in str(i):
        i.json()
    if '<Response [404]>' in str(i):
        "nothing found in this field"

a_data=data[0].text
pprint(a_data)
