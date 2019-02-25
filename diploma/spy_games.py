# вывести список групп в ВК, в которых состоит
# пользователь, но не состоит никто из его друзей.

import requests
import time
import codecs
import json

TOKEN = 'test'

user = input('Введите id пользователя из ВК: ')


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
        print('-', end=" ")
        return res.json()['response']

    def get_group_by_id(self, group_id):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'group_id': group_id,
            'fields': 'members_count'
        }
        res = requests.get('https://api.vk.com/method/groups.getById', params)
        return res.json()['response']


evgeny = User(user)
evgeny_groups = evgeny.get_groups()['items']
evgeny_friends = evgeny.get_friends()['items']
string_of_friends = ','.join([str(x) for x in evgeny_friends])

list_of_groups = []

print('Loading', end=" ")

for group in evgeny_groups:
    group_description = {}
    group_info = evgeny.get_group_by_id(str(group))
    try:
        is_member_in_group = list(filter(lambda x: x['member'] == 1, evgeny.is_member(group, string_of_friends)))
    except KeyError:
        print('Too many requests in one second. Please try again.')
        break
    if len(is_member_in_group) == 0:
        group_description['name'] = group_info[0]["name"]
        group_description['gid'] = group_info[0]["id"]
        group_description['members_count'] = group_info[0]["members_count"]
        list_of_groups.append(group_description)
    time.sleep(2)

with codecs.open('groups.json', 'w', 'utf-8') as file:
    data = list_of_groups
    json.dump(data, file, ensure_ascii=False, indent=2)

print('Finished')
