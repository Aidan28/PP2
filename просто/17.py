import json
people_string = '''
{
    "people": [
        {
            "name": "Aidan",
            "phone": "87769282003",
            "email": "aidana042803@mail.ru"
        },
        {
            "name": "Alan",
            "phone": "87027642449",
            "email": "alan_saudabekov@mail.ru"
        }
    ]
}
'''
data = json.loads(people_string)
for person in data['people']:
    del person['phone']
 
new_string = json.dumps(data, indent = 2)

print(new_string)
  