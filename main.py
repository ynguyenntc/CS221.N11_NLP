import argparse
from ParserModel import Parser


def defineArgument():
    parser = argparse.ArgumentParser()

    # Thêm path Input và output
    parser.add_argument("--Input", help='Input file name')
    parser.add_argument("--Output", help='Output file name')

    # Nhap input số câu và câu cần phân tích từ bàn phím
    parser.add_argument('-n',
                        "--InputFK",
                        action='store_true',
                        help='Input from Keyboard')

    # Cờ để chỉnh path của tập lexicon và grammar nếu cần
    parser.add_argument("-l", "--Lexicon", help='Path to Lexicon file')
    parser.add_argument("-g", "--Grammar", help='Path to Grammar file')

    # Cờ để sử dụng phương pháp tokenizer  của VNCoreNLP
    parser.add_argument("-vn",
                        "--TypeTokenizer",
                        action='store_true',
                        help='Tokenizer by VnCoreNLP')

    # Cờ của StanfordCoreNLP
    parser.add_argument("-st",
                        "--ParserModel",
                        action='store_true',
                        help='Parser by StanfordCoreNLP')
    # Them flags Type Output
    parser.add_argument("-x",
                        "--TypeOuput",
                        action='store_true',
                        help='Get 1 or more output')
    return parser


parser = defineArgument()
args = parser.parse_args()

# CKY
Parser(args.InputFK, args.Input, args.Output, args.Lexicon, args.Grammar,
       args.TypeTokenizer, args.ParserModel, args.TypeOuput)
