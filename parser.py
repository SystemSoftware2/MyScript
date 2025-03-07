#Copyright (c) 2025 System
#This file parses tokens

#Import modules
import sys
from lexer import *
import os
try:
    import keyboard
except:
    if os.name == 'nt':
        os.system('pip install keyboard')
        os.system('cls')
    else:
        os.system('sudo pip install keyboard')
        os.system('clear')
    import keyboard

#Parses tokens
def parse(tokens, env={}):
    pos = 0

    while pos < len(tokens):
        token = tokens[pos]
        if token[1] == 'reserved':
            if token[0] == ':=':
                try:
                    pos -= 1
                    name = tokens[pos][0]
                    
                    pos += 2
                    value = ''

                    while tokens[pos] != (';', 'reserved'):
                        if tokens[pos + 1][0] == ';':
                            value += tokens[pos][0]
                        else:
                            value += tokens[pos][0] + ' '
                        pos += 1

                    env[name] = eval(value, {'__builtins__': env})
                except Exception as err:
                    if not (';', 'reserved') in tokens:
                        sys.stderr.write('SyntaxError: Symbol ";" not found\n')
                    else:
                        sys.stderr.write('Error: '+str(err)+'\n')
            elif token[0] == 'if':
                try:
                    condition = ''
                    code = ''

                    pos += 1
                    while tokens[pos] != ('then', 'reserved'):
                        condition += tokens[pos][0] + ' '
                        pos += 1
                    pos += 1
                    while tokens[pos] != ('end', 'reserved'):
                        code += tokens[pos][0] + '\n'
                        pos += 1

                    condtrue = eval(condition, {'__builtins__': env})

                    if condtrue == True:
                        parse(lex(code))
                    try:
                        if tokens[pos + 1][0] == 'else':
                            code2 = ''
                            pos += 1
                            while tokens[pos] != ('end', 'reserved'):
                                code2 += tokens[pos][0] + '\n'
                                pos += 1
                            if condtrue == False:
                                parse(lex(code2))
                    except:
                        pass
                except Exception as err:
                    if not ('then', 'reserved') in tokens:
                        sys.stderr.write('SyntaxError: Operator "then" not found\n')
                    elif not ('end', 'reserved') in tokens:
                        sys.stderr.write('SyntaxError: Operator "end" not found\n')
                    else:
                        sys.stderr.write('Error: '+str(err)+'\n')
            elif token[0] == 'while':
                try:
                    condition = ''
                    code = ''

                    pos += 1
                    while tokens[pos] != ('do', 'reserved'):
                        condition += tokens[pos][0] + ' '
                        pos += 1
                    pos += 1
                    while tokens[pos] != ('end', 'reserved'):
                        code += tokens[pos][0] + '\n'
                        pos += 1

                    while eval(condition, {'__builtins__': env}):
                        parse(lex(code))
                        if keyboard.is_pressed('e') or keyboard.is_pressed('E'):
                            break
                except Exception as err:
                    if not ('do', 'reserved') in tokens:
                        sys.stderr.write('SyntaxError: Operator "do" not found\n')
                    elif not ('end', 'reserved') in tokens:
                        sys.stderr.write('SyntaxError: Operator "end" not found\n')
                    else:
                        sys.stderr.write('Error: '+str(err)+'\n')
            elif token[0] == 'with':
                try:
                    pos += 1
                    name = token[0]
                    with open(name+'.my', 'r', encoding='utf-8') as f:
                        parse(lex(f.read()))
                except FileNotFoundError:
                    sys.stderr.write('File "%s" not found\n' % name)
                except Exception as err:
                    sys.stderr.write('Error: '+str(err)+'\n')
        pos += 1
    return env
        
def printenv(env):
    print('Final variable values:')
    if env == {}:
        print('Empty')
    else:
        for i in env.keys():
            print(i+': '+str(env[i]))
        env = {}
