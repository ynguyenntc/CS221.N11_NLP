import pandas as pd


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


def Dem_tu_ghep(tokens):
    count_manual_tokenize_compounds = 0
    list_word = []
    for sentence in tokens:
        for word in sentence:
            if '_' in word:
                count_manual_tokenize_compounds += 1
                list_word.append(word)
    # print('Số lượng từ ghép khi tách từ thủ công:', count_manual_tokenize_compounds)
    # print(len(list_word))
    # print(list_word)
    return list_word


thu_cong, _ = Hand('input\data_tokenizer.txt')
vncore, _ = Hand('input\data_tokenizer_vncorenlp.txt')
chinhsua, _ = Hand('input\data_pos_tagging.txt')
list_thucong = Dem_tu_ghep(thu_cong)
list_vncore = Dem_tu_ghep(vncore)
list_chinhsua = Dem_tu_ghep(chinhsua)
# common_s = set(list_thucong) ^ set(list_vncore)
# print(len(common_s))
# for i in common_s:
#     print(i)
print(len(list_chinhsua))

# def createDict(pathRaw='input\data_tokenizer.txt'):
#     list_Tokens = []
#     list = []
#     with open(pathRaw, 'r', encoding="utf-8") as f:
#         data = f.readlines()
#         for line in data:
#             list_Words = line.replace('\n', ' ').split()
#             list.append(list_Words)

#     for i in list:
#         list_Tokens.extend(i)

#     return list_Tokens


# list_Tokens = createDict()
# bi_grams = []
# tri_grams = []
# for sentence in set(list_Tokens):
#     temp = 0
#     for s in list(sentence):
#         if s == "_":
#             temp += 1
#     if temp == 1:
#         bi_grams.append(sentence)
#     elif temp == 2:
#         tri_grams.append(sentence)
# list_tu = []
# list_tu.extend(bi_grams)
# list_tu.extend(tri_grams)
# print(list_tu)
# print(len(list_tu))'
# for sentence in set(list_Tokens):
#     if '_' in sentence:
#         list_tu.append(sentence)

# print(list_tu)


# def count_correct_words(pred, source, n_grams=3):
#     pred_words = pred.split()
#     source_words = source.split()

#     total_true, tp = 0, 0
#     total_errors, fp = 0, 0

#     idx = 0
#     while idx < len(pred_words):
#         if pred_words[idx] not in source_words[idx:(idx + n_grams)]:
#             if '_' in pred_words[idx]:
#                 fp += 1
#             del pred_words[idx]
#             total_errors += 1
#         else:
#             idx += 1

#     idx = 0
#     while idx < len(source_words):
#         if source_words[idx] not in pred_words[idx:(idx + n_grams)]:
#             del source_words[idx]
#         else:
#             idx += 1

#     if len(pred_words) < len(source_words):
#         words = pred_words
#     else:
#         words = source_words

#     for idx in range(len(words)):
#         if pred_words[idx] == source_words[idx]:
#             if '_' in pred_words[idx]:
#                 tp += 1
#             total_true += 1

#     return total_true, total_errors, tp, fp


# def tokenize_evaluation(pred, source, n_grams=3):
#     total_true = 0
#     total_errors = 0
#     total_words = 0

#     pred_tp = 0
#     pred_fp = 0

#     for pred_sentence, source_sentence in zip(pred, source):
#         total_words += len(source_sentence.split())
#         if pred_sentence != source_sentence:
#             true, error, tp, fp = count_correct_words(
#                 pred_sentence, source_sentence, n_grams)
#             total_true += true
#             total_errors += error
#             pred_tp += tp
#             pred_fp += fp
#         else:
#             for word in source_sentence.split():
#                 if '_' in word:
#                     pred_tp += 1
#                 total_true += 1
#     return {
#         'Accuracy': total_true / total_words,
#         'Precision': pred_tp / (pred_tp + pred_fp),
#         'Recall': pred_tp / count_manual_tokenize_compounds,
#         'True Positive': pred_tp,
#         'False Positive': pred_fp,
#         'Total True': total_true,
#         'Total Errors': total_errors
#     }

# longest_matching_evaluation = tokenize_evaluation(longest_matching_sentences, manual_tokenize_sentences)
# vncore_evaluation = tokenize_evaluation(vncore_sentences, manual_tokenize_sentences)
# pd.DataFrame(
#     [longest_matching_evaluation, vncore_evaluation],
#     index = ['Longest Matching', 'VnCoreNLP']
# ).astype(object).T
