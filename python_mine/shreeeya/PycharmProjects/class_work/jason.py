import json
json_string = """
    {
        "people": [
            {
                "name": "Sagar Giri",
                "phone": ["9807360000", "9840207890"],
                "emails": "girisagar46@gmail.com",
                "has_license": false
            },
            {
                "name": "Ram Bahadur",
                "phone": ["9800000000"],
                "emails": null,
                "has_license": true
            }
        ]
    }
"""

#data = json.loads(json_string)
#print(type(data))



data= json.loads(json_string)
#l=data['people']
 #for each in l:
         #print(each.get("name"),each.get("phone"))


l=data['people']
for each in l:
    if each.get('has_license'):
        print(each.get('name'))


for person in data["people"]:
     print(person["phone"])




