import pickle


def createDict(pathRaw='input\data_tokenizer.txt'):
    list_Tokens = []
    list = []
    with open(pathRaw, 'r', encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            list_Words = line.replace('\n', ' ').split()
            list.append(list_Words)

    for i in list:
        list_Tokens.extend(i)

    return list_Tokens


list_Tokens = createDict()
# count_compounds = 0
# for sentence in list_Tokens:
#     for word in sentence:
#         if '_' in word:
#             count_compounds += 1
#print('Số lượng từ ghép khi tách từ thủ công:', count_compounds)
# print(list_Tokens)
bi_grams = []
tri_grams = []
for sentence in set(list_Tokens):
    temp = 0
    for s in list(sentence):
        if s == "_":
            temp += 1
    if temp == 1:
        bi_grams.append(sentence)
    elif temp == 2:
        tri_grams.append(sentence)
print(len(bi_grams))
print(len(tri_grams))

# print(list_Tokens)

pickle.dump(list_Tokens, open('input/dictionary.pkl', 'wb'))

# with open('input/dictionary.pkl', 'rb') as f:
#     data = pickle.load(f)
# print(data)


# with open('input\dictionary.txt', 'w', encoding="utf-8") as f:
#     for i in list_Tokens:
#             f.write(i)
#             f.write('\n')
