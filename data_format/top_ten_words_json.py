# Get top ten words from JSON file
import json


def get_news():
    with open('newsafr.json', encoding='utf-8') as news_obj:
        news = json.load(news_obj)
    return news


def get_items_list(news):
    return news['rss']['channel']['items']


def get_words_dict(items):
    words_dict = {}
    for item in items:
        splited_words = item['description'].split()
        for word in splited_words:
            word = word.lower()
            if word.isdigit() or len(word) <= 6:
                continue
            if words_dict.get(word):
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return words_dict


def get_top_ten_words(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:10]


def print_top_ten_words(words):
    for word in words:
        print(f'Word: {word[0]} - meets {word[1]} times')


all_news = get_news()
items_list = get_items_list(all_news)
all_words_dict = get_words_dict(items_list)
top_ten_words = get_top_ten_words(all_words_dict)
print_top_ten_words(top_ten_words)

