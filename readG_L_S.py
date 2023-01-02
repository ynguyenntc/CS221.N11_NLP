# Import module Tokenizer là maximumMatching để thực hiện tách từ
from tokenizer_maximum_matching import maximumMatching


def readGrammar(path2Grammar='input/grammar_CNF.txt'):
    # Đọc tập Grammar như đã trình bày ở bước 1 trong Báo Cáo
    # Được định dạng là 1 grammar có cấu trúc là X -> Y1, Y2
    with open(path2Grammar, 'r') as f:
        list_lines = f.read().split('\n')
        list_Grammars = []
        for idx, line in enumerate(list_lines):
            if line.startswith('#') or line == '':
                continue
            list_Words = line.split()
            if len(list_Words) == 4:

                grammar = dict()
                # x -> y1 y2
                grammar['X'] = list_Words[0]
                grammar['Y1'] = list_Words[2]
                grammar['Y2'] = list_Words[3]
                list_Grammars.append(grammar)

            else:
                print('Ngữ pháp lỗi %d' % (idx + 1))

        return list_Grammars

    print('Không tồn tại ngữ pháp ở trong tập grammar')
    return []


def readLexicon(path2Lexicon='input/lexicon.txt'):
    # Đọc tập Lexicon như ở bước 1
    # Tập Lexicon có cấu trúc từng dòng là X -> Y
    with open(path2Lexicon, 'r', encoding='utf-8') as f:
        list_lines = f.read().split('\n')
        list_Lexicons = []
        for idx, line in enumerate(list_lines):
            if line.startswith('#') or line == '':
                continue
            list_Words = line.split()
            if len(list_Words) == 3:

                lexicon = dict()
                # X -> Y
                lexicon['X'] = list_Words[0]
                lexicon['Y'] = list_Words[2]

                list_Lexicons.append(lexicon)

            else:
                print('Lexicon lỗi {}'.format(idx + 1))

        return list_Lexicons

    print('Không tìm thấy cấu trúc Lexicon ở trong tập đã cho! ')
    return []


def readSentence(path2Sentence='input/data_raw.txt'):
    # Đọc các câu Sentence

    with open(path2Sentence, 'r', encoding='utf-8') as f:
        list_Lines = f.read().split('\n')
    if list_Lines:
        return list_Lines

    print('Không tìm thấy Sentence!')
    return []
