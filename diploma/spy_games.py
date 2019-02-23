# вывести список групп в ВК, в которых состоит
# пользователь, но не состоит никто из его друзей.

from utils import get_token
import requests
import time
import codecs

TOKEN = get_token()


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_groups(self):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'user_id': self.user_id,
        }
        res = requests.get('https://api.vk.com/method/groups.get', params)
        return res.json()['response']

    def get_friends(self):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'user_id': self.user_id
        }
        res = requests.get('https://api.vk.com/method/friends.get', params)
        return res.json()['response']

    def get_group_members(self, group_id):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'group_id': group_id,
        }
        res = requests.get('https://api.vk.com/method/groups.getMembers', params)
        return res.json()['response']


evgeny = User('171691064')

evgeny_groups = evgeny.get_groups()['items']
evgeny_friends = evgeny.get_friends()

print(evgeny_groups)
print(evgeny_friends)

for group in evgeny_groups:
    group_members = evgeny.get_group_members(group)
    # with codecs.open('groups_info.py', 'a', 'utf-8') as file:
    #     file.write(str(group_info) + '\n')
    print(group_members)
    time.sleep(2)

