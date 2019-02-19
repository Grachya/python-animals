import requests
import time

TOKEN = 'bd878a0562f9e0a7b89fbbc575c60f7a9dc67df73c5b7ab25cb556a9aa71f8ecc0c069671657694e88d7f'

class User:
    def __init__(self, user_id=None):
        self.user_id = user_id

    def __str__(self):
        return self.get_profile_url()

    def __and__(self, other):
        left_operand_friends = self.get_friends(self.user_id)
        right_operand_friends = self.get_friends(other.user_id)

        return self.get_intersection(left_operand_friends, right_operand_friends)

    def get_profile_url(self):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
            'user_id': self.user_id,
            'fields': 'screen_name'
        }
        res = requests.get(
            'https://api.vk.com/method/users.get',
            params)

        screen_name = res.json()['response'][0]['screen_name']
        profile_url = f'https://vk.com/{screen_name}'
        return profile_url

    def get_friends(self, user_id=None):
        params = {
            'v': '5.92',
            'access_token': TOKEN,
        }
        if user_id:
            params['user_id'] = user_id
        res = requests.get(
            'https://api.vk.com/method/friends.get',
            params)
        return res.json()['response']['items']

    def get_intersection(self, list_1, list_2):
        common_friends = list(set(list_1) & set(list_2))

        intersection_friends = []
        for friend in common_friends:
            user = User(friend)
            intersection_friends.append(user)
        return intersection_friends


some_friend_id = '143058'

user_1 = User()
user_2 = User(some_friend_id)

print(f'Ссылка на профиль пользователя 1: {user_1}')
print(f'Ссылка на профиль пользователя 2: {user_2}')

common = user_1 & user_2

for item in common:
    print(f'Профиль обещего друга: {item}')
    time.sleep(1)


