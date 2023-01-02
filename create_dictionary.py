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

# def createDict(pathRaw='input\data_tokenizer.txt'):
#     with open(pathRaw, 'r', encoding="utf-8") as f:
#         data = f.read()
#         lines = data.split('\n')

#     tokens = []
#     list_Tokens = []
#     for i in lines:
#         token = i.split()
#         tokens.append(token)
#     for i in tokens:
#         list_Tokens.extend(i)
#     return list_Tokens


list_Tokens = createDict()


# def Dem_tu_ghep(tokens):
#     count_manual_tokenize_compounds = 0
#     list_word = []
#     for word in tokens:
#         if '_' in word:
#             count_manual_tokenize_compounds += 1
#             list_word.append(word)
#     # print('Số lượng từ ghép khi tách từ thủ công:', count_manual_tokenize_compounds)
#     # print(len(list_word))
#     # print(list_word)
#     return list_word


#list_thucong = Dem_tu_ghep(list_Tokens)
# print(len(list_thucong))
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
# pickle.dump(bi_grams, open('input/bi_grams.pkl', 'wb'))
# pickle.dump(tri_grams, open('input/tri_grams.pkl', 'wb'))


# pickle.dump(list_Tokens, open('input/dictionary.pkl', 'wb'))


# with open('input/dictionary.pkl', 'rb') as f:
#     data = pickle.load(f)
# print(data)


# with open('input\dictionary.txt', 'w', encoding="utf-8") as f:
#     for i in list_Tokens:
#             f.write(i)
#             f.write('\n')
