import pickle
from collections import defaultdict
import unicodedata as ud
import pandas as pd
import numpy as np
import math
import ast
import re


def getDictionary(path2Dictionary='input/Dictionary.pkl'):
    list_Words = pickle.load(open(path2Dictionary, 'rb'))
    return list_Words


def syllablize(sentence):
    word = '\w+'
    non_word = '[^\w\s]'
    digits = '\d+([\.,_]\d+)+'

    patterns = []
    patterns.extend([word, non_word, digits])
    patterns = f"({'|'.join(patterns)})"

    sentence = ud.normalize('NFC', sentence)
    tokens = re.findall(patterns, sentence, re.UNICODE)
    return [token[0] for token in tokens]


def maximumMatching(sentence, maxlen=4):
    dictionary = getDictionary()

    my_list = []
    list_Words = sentence.split()
    len_now = len(list_Words)
    i = 0
    maxl = maxlen
    while i < len_now:
        wordCheck = '_'.join(list_Words[i:maxlen + i])

        while wordCheck not in dictionary:
            if maxl > 1:
                wordCheck = '_'.join(list_Words[i:i + maxl])
            elif maxl == 1:
                wordCheck = list_Words[i]
            elif maxl == 0:
                break
            maxl -= 1
        if maxl > 0:
            i += maxl
        i += 1
        my_list.append(wordCheck)
        maxl = min(len_now - i, maxlen)

    line = ' '.join(my_list)

    return line


def maximumsMatching(lines, maxlen=4):
    '''
        Tach nhieu cau bang Maximum Matching
    '''
    dictionary = getDictionary()

    list_Tokenizer = []
    list = []
    list_Lines = []
    for line in lines:
        my_list = []
        list_Words = syllablize(line)
        len_now = len(list_Words)
        i = 0
        maxl = maxlen
        while i < len_now:
            wordCheck = '_'.join(list_Words[i:maxlen + i])

            while wordCheck not in dictionary:
                #  print(wordCheck)
                if maxl > 1:
                    wordCheck = '_'.join(list_Words[i:i + maxl])
                elif maxl == 1:
                    wordCheck = list_Words[i]
                elif maxl == 0:
                    break
                maxl -= 1
            if maxl > 0:
                i += maxl
            i += 1
            #  print('TRUE {} | Len: {}'.format(wordCheck, maxl))
            my_list.append(wordCheck)
            maxl = min(len_now - i, maxlen)

        list_Lines.append(' '.join(my_list))
        list_Tokenizer.append(my_list)

    for i in list_Tokenizer:
        list.extend(i)

    return list_Lines, list


with open('input/data_raw.txt', 'r', encoding="utf-8") as f:
    data = f.read()
    lines = data.split('\n')
list_line, list_token = maximumsMatching(lines)
#print(list_line, list_token)

bi_grams = []
tri_grams = []
for word in list_token:
    temp = 0
    temp = word.count('_')
    if temp == 1:
        bi_grams.append(word)
    elif temp == 2:
        tri_grams.append(word)
print(len(bi_grams))
print(len(tri_grams))

#  pickle.dump(list_Tokens, open('output/maximumMatching.pkl', 'wb'))
#
with open('input\data_tokenizer_maximum_matching.txt', 'w', encoding="utf-8") as f:
    for line in list_line:
        f.write(line)
        f.write('\n')
