import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)