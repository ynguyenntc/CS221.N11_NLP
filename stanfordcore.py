from stanfordnlp.server import CoreNLPClient

client = CoreNLPClient(start_server=False)


def printTree(tree):
    ret = tree.value
    if len(tree.child) > 0:
        ret = "(" + ret + " "
        for child in tree.child:
            ret = ret + " " + printTree(child)

        ret = ret + ")"
    return ret


def STParser(text):
    ann = client.annotate(text,
                          properties={
                              'annotators': 'parse',
                              'parse.model': 'VnParser2.ser.gz'
                          })
    sentences = ann.sentence
    try:
        sentence = sentences[0]
        temp = printTree(sentence.parseTree).replace('  ', ' ').replace(
            '(ROOT ', '')[:-1]
        return [temp]
    except:
        return ['[ERROR] ' + text]
