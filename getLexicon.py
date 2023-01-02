import re


def getLexicon(path2Lexicon='input/data_gold.txt'):
    with open(path2Lexicon, 'r', encoding="utf-8") as f:

        data = f.read()

    list_Lexicons = re.findall('(\w+\s\w+)', data)

    print(re.findall('(PU\s\W)', data))

    list_Lexicons += re.findall('(PU\s\W)', data)
    return list(set(list_Lexicons))


def getLabel(path2Label='input/data_gold.txt'):
    pass


# with open("input/lexicon.txt", 'w', encoding="utf-8") as f:
#     list_Lexicons = getLexicon()
#     for lexicon in list_Lexicons:
#         f.write(lexicon.replace(' ', ' -> '))
#         f.write('\n')

# a = getLexicon()
# print(a)
