from urllib.parse import urlencode


def get_url_for_token():
    oauth_url = 'https://oauth.vk.com/authorize'
    params = {
        'client_id': 6862253,
        'display': 'page',
        'scope:': 'status,friends,groups',
        'response_type': 'token',
        'v': 5.92
    }

    return f'{oauth_url}?{urlencode(params)}'


def get_token():
    return 'a50c2d4acdd2d7aa69785961844ed4bc7aaa6d8891bd6fdd33bd825d89970b63be48458d4952095d9bd61'
