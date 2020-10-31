# Convert string to camel case
# https://www.codewars.com/kata/517abf86da9663f1d2000003


def to_camel_case(text):
    if text:
        words = text.replace('-', ' ').replace('_', ' ').split()
        text = "".join([word.title() if index > 0 else word for index, word in enumerate(words)])
    return text
