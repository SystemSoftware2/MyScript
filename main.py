#Copyright (c) 2025 System

import sys
from lexer import *
from parser import *

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(1)
    try:
        poss = 1
        while poss < len(sys.argv):
            with open(sys.argv[poss], 'r', encoding='utf-8') as f:
                code = f.read()
                parse(lex(code))
            poss += 1
    except:
        sys.exit(1)
