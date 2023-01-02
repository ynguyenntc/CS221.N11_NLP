from vncorenlp import VnCoreNLP
rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar",
                         annotators="wseg,pos",
                         max_heap_size='-Xmx1g')


path = 'input\data_gold_tokenizer.txt'


def Hand(path):
    list_Tokens = []
    with open(path, 'r', encoding="utf-8") as f:
        data = f.read()
        lines = data.split('\n')

    tokens = []
    for i in lines:
        token = i.split()
        tokens.append(token)

    for i in tokens:
        list_Tokens.extend(i)
    return list_Tokens


manual_tokens = Hand(path)
# with open('input\pos_vncore.txt', 'w', encoding="utf-8") as f:
#     for i in manual_tokens:
#         f.write(i)
#         f.write('\n')
# manual_tokens = Hand(path)
# list = []
# for word in manual_tokens:
#     word = word.replace('\n', '')
#     print(word)


with open('input\pos_vncore.txt', 'w', encoding='utf-8') as f:
    for word in manual_tokens:
        word = word.replace('\n', '')

        if '_' not in word:
            tag = rdrsegmenter.pos_tag(word)
        else:
            tag = rdrsegmenter.pos_tag(word.replace('_', ' '))

        if tag == []:
            f.write('\n')
        else:
            f.write(f'{word}\t{tag[0][0][1]}\n')
    f.write('\n')
