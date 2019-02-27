import requests
import time
import copy
import codecs
import json

TOKEN = '<Enter your token>'

user_input = input('Введите id пользователя из ВК: ')
user_input.strip()

print('Loading', end=" ")


class User:
    def __init__(self, user, token):
        self.default_params = {
            'v': '5.92',
            'access_token': token,
        }
        self.evgeny_groups = None
        self.evgeny_friends = None
        self.list_of_groups = []
        if user.isdigit():
            self.user_id = user
        else:
            self.user_id = str(self.get_user_id(user))

    def get_user_id(self, usr):
        local_params = copy.copy(self.default_params)
        local_params['fields'] = 'screen_name'
        local_params['user_ids'] = usr
        res = requests.get('https://api.vk.com/method/users.get', local_params)
        print('-', end=" ")
        return res.json()['response'][0]['id']

    def get_groups(self):
        local_params = copy.copy(self.default_params)
        local_params['user_id'] = self.user_id
        res = requests.get('https://api.vk.com/method/groups.get', local_params)
        print('-', end=" ")
        return res.json()['response']

    def get_friends(self):
        local_params = copy.copy(self.default_params)
        local_params['user_id'] = self.user_id
        res = requests.get('https://api.vk.com/method/friends.get', local_params)
        print('-', end=" ")
        return res.json()['response']

    def is_member_of_group(self, group_id, user_ids):
        local_params = copy.copy(self.default_params)
        local_params['group_id'] = group_id
        local_params['user_ids'] = user_ids
        res = requests.get('https://api.vk.com/method/groups.isMember', local_params)
        print('-', end=" ")
        return res.json()['response']

    def get_group_by_id(self, group_id):
        local_params = copy.copy(self.default_params)
        local_params['group_id'] = group_id
        local_params['fields'] = 'members_count'
        res = requests.get('https://api.vk.com/method/groups.getById', local_params)
        print('-', end=" ")
        return res.json()['response']

    def is_member(self, group, friends):
        return list(filter(lambda x: x['member'] == 1, self.is_member_of_group(group, friends)))

    def append_to_list(self, is_member, group_info):
        group_description = {}
        if len(is_member) == 0:
            group_description['name'] = group_info[0]["name"]
            group_description['gid'] = group_info[0]["id"]
            group_description['members_count'] = group_info[0]["members_count"]
            self.list_of_groups.append(group_description)
            return group_description

    def get_groups_without_friends(self):
        self.evgeny_groups = self.get_groups()['items']
        self.evgeny_friends = self.get_friends()['items']
        string_of_friends = ','.join([str(x) for x in self.evgeny_friends])

        for group in self.evgeny_groups:
            try:
                group_info = self.get_group_by_id(str(group))
                is_member_in_group = self.is_member(group, string_of_friends)
            except KeyError:
                time.sleep(2)
                group_info = self.get_group_by_id(str(group))
                is_member_in_group = self.is_member(group, string_of_friends)
            self.append_to_list(is_member_in_group, group_info)
        return self.list_of_groups


evgeny = User(user_input, TOKEN)
groups_without_friends = evgeny.get_groups_without_friends()

with codecs.open('groups.json', 'w', 'utf-8') as file:
    data = groups_without_friends
    json.dump(data, file, ensure_ascii=False, indent=2)

print('Finished')
print('File groups.json is ready')

