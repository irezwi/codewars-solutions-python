# Convert string to camel case
# https://www.codewars.com/kata/517abf86da9663f1d2000003


def to_camel_case(text):
    words = list(text.replace('-', ' ').replace('_', ' ').split())
    for i in range(1, len(words)):
        words[i] = words[i].title()
    return "".join(words)
