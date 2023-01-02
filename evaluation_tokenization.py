import pickle


def Hand(path):
    with open(path, 'r', encoding="utf-8") as f:
        data = f.read()
        lines = data.split('\n')

    tokens = []
    list_Tokens = []
    for i in lines:
        token = i.split()
        tokens.append(token)
    for i in tokens:
        list_Tokens.extend(i)
    return tokens, list_Tokens

#     pickle.dump(tokens, open('output/data_tokenizer.pkl', 'wb'))


path = 'input\data_tokenizer.txt'
path_vncore = 'input\data_tokenizer_vncorenlp.txt'
path_max_matching = 'input\data_tokenizer_maximum_matching.txt'
path_chinhsua = 'input\data_pos_tagging.txt'
# print(Hand(path_vncore))
# y_pre, _ = Hand('input\data_tokenizer.txt')
# print(y_pre)


_, tokens = Hand(path)
_, tokens_vncore = Hand(path_vncore)
_, tokens_max_matching = Hand(path_max_matching)
_, tokens_chinhsua = Hand(path_chinhsua)
# print(len(tokens), len(tokens_vncore), len(tokens_max_matching))


def different_tokens(l1, l2):
    common_s = set(l1) ^ set(l2)
    for i in common_s:
        print(i)


different_tokens(tokens, tokens_vncore)


def Token_Eva(path2Tokenizer):
    '''
    Danh gia precision va recall cua tokenizer
    '''
    # pre = pickle.load(open(path2Tokenizer, 'rb'))
    y_pre, _ = Hand(path2Tokenizer)
    # y = pickle.load(open('input\dictionary.pkl', 'rb'))
    y, _ = Hand(path)

    precision = 0
    recall = 0

    for idx, i in enumerate(y_pre):
        inpre = [x for x in i if x not in y[idx]]

        s = sum([i.count(x) for x in inpre])

        # if len(i) - s > 0:
        #     print(i)
        precision += (len(i) - s) / len(i)
        recall += (len(i) - s) / len(y[idx])

    precision, recall = precision / len(y_pre) * 100, recall / len(y_pre) * 100
    # f1_score = 2*(precision * recall)/(precision + recall)
    print('Precision : {} | Recall: {}'.format(precision, recall))
    # return precision, recall


print('VNcore:')
Token_Eva(path_vncore)
print('Maximum Matching:')
Token_Eva(path_max_matching)
