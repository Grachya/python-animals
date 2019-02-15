import requests

TOKEN = 'e9dcdb57d7f7eb72a0a962bed4549466b01c5e581875f95c037b4246baaca5289969fce94a724a1f286b5'

class User:
    def __init__(self, token):
        self.token = token

    def get_friends(self, user_id=''):
        params = {
            'v': '5.92',
            'access_token': self.token,
        }
        if user_id:
            params['user_id'] = user_id
        res = requests.get(
            'https://api.vk.com/method/friends.get',
            params)
        return res.json()['response']['items']

    def get_users(self, user_ids):
        params = {
            'v': '5.92',
            'access_token': self.token,
            'user_ids': user_ids,
            'fields': 'true',
        }
        res = requests.get(
            'https://api.vk.com/method/users.get',
            params)
        return res.json()

    def get_intersection(self, list_1, list_2):
        inters = list(set(list_1) & set(list_2))
        for k, item in enumerate(inters):
            inters[k] = str(item)
        return ','.join(inters)


user = User(TOKEN)
own_friends = user.get_friends()
x_friend = own_friends[0]
x_friend_name = user.get_users(x_friend)
x_friend_friends = user.get_friends(x_friend)
intersection = user.get_intersection(own_friends, x_friend_friends)
intersection_users = user.get_users(intersection)['response']

print(f'Наши общие друзья с {x_friend_name["response"][0]["first_name"]}:')
for user in intersection_users:
    print(user['first_name'], user['last_name'])
