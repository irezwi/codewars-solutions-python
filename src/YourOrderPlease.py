import re


def order(sentence):
    res = []
    n_order = re.findall(r'\d+', sentence)
    sen = sentence.split()
    for i in range(0, len(sen)):
        res.insert(int(n_order[i]) - 1, sen[i])
    return " ".join(res)
