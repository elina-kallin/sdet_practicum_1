import random


def generate_post_code(length):
    str_code = ""
    for each in range(length):
        str_code = str_code + str(random.randint(0, 9))
    print(str_code)
    return str_code


def generate_first_name(post_code):
    name = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(post_code), 2):
        pair = post_code[i : i + 2]
        num = int(pair)
        letter = alphabet[num % 26]
        name += letter
    name[0].upper
    return name
