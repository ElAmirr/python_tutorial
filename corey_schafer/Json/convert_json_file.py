import json
# open and loads json string into python file
with open('states.json') as rf:
    data = json.load(rf)
    for state in data['states']:
        del state['abbreviation']
# write and dumps python object to json string
with open('new_states.json', 'w') as wf:
    json.dump(data, wf, indent=2)
