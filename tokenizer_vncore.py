from vncorenlp import VnCoreNLP
rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar",
                         annotators="wseg",
                         max_heap_size='-Xmx1g')


def wordTokenzizer(sentence):
    '''
    Tach tu voi thu vien VnCoreNLP
    '''
    token = [i for j in rdrsegmenter.tokenize(sentence) for i in j]
    return ' '.join(token)


def wordsTokenzizer(path2Raw='input/data_raw.txt'):
    '''
    Tach nhieu cau thanh tu voi thu vien VnCoreNLP
    '''
    list_Tokens = []
    list_LinesTokens = []
    list = []
    with open(path2Raw, 'r', encoding="utf-8") as f:
        data = f.read()

        list_Lines = data.split('\n')
        for line in list_Lines:
            token = [i for j in rdrsegmenter.tokenize(line) for i in j]

            list_LinesTokens.append(' '.join(token))
            list_Tokens.append(token)

    for i in list_Tokens:
        list.extend(i)

    return list, list_LinesTokens


list_Tokens, list_LinesTokens = wordsTokenzizer()
# print(list_Tokens)
# print(list_LinesTokens)
#pickle.dump(list_Tokens, open('output/VnCore_Tokens.pkl', 'wb'))
# print(list_Tokens)
bi_grams = []
tri_grams = []
for word in list_Tokens:
    temp = 0
    temp = word.count('_')
    if temp == 1:
        bi_grams.append(word)
    elif temp == 2:
        tri_grams.append(word)
print(len(bi_grams))
print(len(tri_grams))


# print(list_LinesTokens)
with open('input\data_tokenizer_vncorenlp.txt', 'w', encoding="utf-8") as f:
    for line in list_LinesTokens:
        f.write(line)
        f.write('\n')
