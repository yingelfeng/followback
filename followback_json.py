import json

with open('followers_1.json', 'r') as f:
    followers_data = json.load(f)
    followers = [entry['string_list_data'][0]['value'] for entry in followers_data]

with open('following.json', 'r') as f:
    following_data = json.load(f)
    entries = following_data["relationships_following"]
    following = [entry['string_list_data'][0]['value'] for entry in entries]


not_following_back = [user for user in following if user not in followers]

print("People who don’t follow you back:")
for user in not_following_back:
    print(user)
