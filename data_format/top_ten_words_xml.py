import xml.etree.ElementTree as ET


def get_root():
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    return root


def get_all_items(root):
    return root.findall("channel/item")


def get_words_dict(items):
    words_dict = {}
    for item in items:
        splited_words = item.find('description').text.split()
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


root_tag = get_root()
all_items = get_all_items(root_tag)
all_words_dict = get_words_dict(all_items)
top_ten_words = get_top_ten_words(all_words_dict)
print_top_ten_words(top_ten_words)

