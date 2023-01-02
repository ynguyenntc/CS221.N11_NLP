from CKY import syntacticAnalyzer
from readG_L_S import readSentence
from tokenizer_maximum_matching import maximumMatching
from tokenizer_vncore import wordTokenzizer
from stanfordcore import STParser


def Parser(intk, Input, Output, lexicon, grammar, TypeTokenizer, ParserModel,
           TypeOuput):
    s = 0
    if intk:
        n = int(input('Nhap so cau'))
        list_Sentences = []
        for i in range(n):
            list_Sentences.append(input())
    else:
        if Input:
            list_Sentences = readSentence(Input)
        else:
            list_Sentences = readSentence()

    list_Results = []
    for idx, sentence in enumerate(list_Sentences):
        if TypeTokenizer:
            sentence = wordTokenzizer(sentence)
        else:
            sentence = maximumMatching(sentence)
        if ParserModel:
            result = STParser(sentence)
        else:
            result = syntacticAnalyzer(sentence, lexicon, grammar)

        try:
            if TypeOuput:
                list_Results.append(result)
            else:
                list_Results.append([result[0]])
        except:
            list_Results.append([])
        if len(result) > 0:
            s += 1
    if Output:
        with open(Output, 'w') as f:
            for i in range(len(list_Sentences)):
                f.write(list_Sentences[i])
                f.write('\n')
                try:
                    f.writelines(list_Results[i])
                except:
                    pass

                f.write('----------------------------------------------\n')
    else:
        for i in range(len(list_Sentences)):
            print('Num: %d| %s' % (i + 1, list_Sentences[i]))
            try:
                for j in list_Results[i]:
                    print(j)
            except:
                print()
            print('----------------------------------------------\n')
