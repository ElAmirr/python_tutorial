import json
people_string = '''
{
    "people": [
        { 
            "name": "Amir Othmani",
            "phone": "+216 92 104 649",
            "emails": ["othmaniamir41@gmail.co", "elothmanielamir@gmail.com"],
            "hase_license": false
        },
        {
            "name": "Skandar Othmani",
            "phone": "+216 21 239 352",
            "emails": null,
            "hase_license": true
        }
    ]
}

'''
# loads json string into python file
data = json.loads(people_string)
for person in data['people']:
    del person['phone']

# dumps python object to json string
new_string = json.dumps(data, indent=2)

print(new_string)
