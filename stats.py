def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(content):
    return len(content.split())

def count_chars(content):
    lowered_text = content.lower()
    char_dic = {}
    for char in lowered_text:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

def sort_on(items):
    return items["num"]

def sort(items):
    sorted_list = []

    for item in items:
        if item.isalpha():
            new_dic = {}
            new_dic["char"] = item
            new_dic["num"] = items[item]
            sorted_list.append(new_dic)



    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list