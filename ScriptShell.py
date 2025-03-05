from lexer import *
from parser import *
from datetime import *
import sys

class Program:
    def __init__(self):
        self.text = ''

    def add(self, text):
        self.text += text

    def clear(self):
        self.text = ''
        
    def open(self, name):
        try:
            with open(name, 'r', encoding='utf-8') as f:
                self.text = f.read()
        except:
            sys.stderr.write('File not found\n')

    def programtext(self):
        lines = self.text.split('\n')
        for i in lines:
            if i == '':
                pass
            else:
                print(i)

    def run(self):
        printenv(parse(lex(self.text)))

class Shell:
    def __init__(self):
        self.program = Program()

    def check(self, text):
        if text == 'exit':
            sys.exit(1)
        elif text == 'run':
            self.program.run()
        elif text == "list":
            self.program.programtext()
        elif text == "clear":
            self.program.clear()
        else:
            self.program.add(text+'\n')

    def start(self):
        print('Welcome to ScriptShell.\nTime: '+str(datetime.now().replace(microsecond=0))+'. This is the console for the MyScript programming language.\nCommands: exit, run, list, clear.')
        while True:
            com = input('>>> ')
            self.check(com)

if __name__ == '__main__':
    shell = Shell()
    shell.start()
