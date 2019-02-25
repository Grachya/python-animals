# вывести список групп в ВК, в которых состоит
# пользователь, но не состоит никто из его друзей.

import requests
import time

TOKEN = 'bd1d62485df3c40b2c192b088e445d08b35c358738947d913caf694ef8b6dfed41fa25eb6f40e0b4abe1d'


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

    def is_member(self, group_id, user_ids):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'group_id': group_id,
            'user_ids': user_ids
        }
        res = requests.get('https://api.vk.com/method/groups.isMember', params)
        return res.json()['response']

    def get_group_by_id(self, group_id):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'group_id': group_id,
        }
        res = requests.get('https://api.vk.com/method/groups.getById', params)
        return res.json()['response']


evgeny = User('171691064')
evgeny_groups = evgeny.get_groups()['items']
evgeny_friends = evgeny.get_friends()['items']
string_of_friends = ','.join([str(x) for x in evgeny_friends])

for group in evgeny_groups:
    group_info = evgeny.get_group_by_id(str(group))
    is_member_in_group = list(filter(lambda x: x['member'] == 1, evgeny.is_member(group, string_of_friends)))
    if len(is_member_in_group) == 0:
        print(f'В группе {group_info[0]["name"]} ни состоит ни один из его друзей')
    time.sleep(2)
