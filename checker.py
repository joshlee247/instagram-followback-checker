import json

followers = set()
following = set()

# Opening JSON file
f1 = open('followers.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f1)
  
# Iterating through the json
# list
for i in data['relationships_followers']:
    followers.add(i['string_list_data'][0]['value'])

# Closing file
f1.close()

# Opening JSON file
f2 = open('following.json')

# returns JSON object as 
# a dictionary
data = json.load(f2)  

for i in data['relationships_following']:
    following.add(i['string_list_data'][0]['value'])

# Closing file
f2.close()

for i in following.difference(followers):
    print(i)

print()
print(len(following.difference(followers)))
