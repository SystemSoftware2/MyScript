#Copyright (c) 2025 System
#This is lexer

INT = 'int'
FLOAT = 'float'
ID = 'id'
BOOL = 'bool'
RESERVED = 'reserved'

keywords = [
    ('if', RESERVED),
    ('then', RESERVED),
    (':=', RESERVED),
    ('end', RESERVED),
    ('while', RESERVED),
    ('do', RESERVED),
    ('-', RESERVED),
    ('*', RESERVED),
    ('/', RESERVED),
    ('+', RESERVED),
    ('>', RESERVED),
    ('<', RESERVED),
    ('==', RESERVED),
    ('!=', RESERVED),
    (';', RESERVED),
    ('else', RESERVED)
]

def iskeyword(value):
    for i in keywords:
        if i[0] == value:
            return True
        else:
            pass
    return False

def is_float(value):
    try:
        if value == '':
            return False
        float(value)
        return True
    except:
        return False

def lex(characters):
  tokens = []
  lines = characters.split('\n')

  for line in lines:
    value = line.split(' ')
    for pos in value:
      for i in keywords:
        if i[0] == pos:
          tokens.append(i)
      if pos == 'true':
        tokens.append(('True', BOOL))
      elif pos == 'false':
        tokens.append(('False', BOOL))
      elif pos.isdigit():
        tokens.append((pos, INT))
      elif is_float(pos):
        tokens.append((pos, FLOAT))
      else:
          if iskeyword(pos):
              pass
          elif pos == '':
              pass
          else:
            tokens.append((pos, ID))
  return tokens
