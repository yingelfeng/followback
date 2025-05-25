def difference (following, followers):
    return [item for item in following if item not in followers]

def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]
    
def delete_dates(list):
    return [item for item in list if not item.endswith('m')]

following = read_list_from_file('following.txt')
followers = read_list_from_file('followers.txt')

result = difference(following, followers)
final = delete_dates(result)

print("People who don't follow you back:", final)
