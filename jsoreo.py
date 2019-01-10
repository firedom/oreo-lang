import os, sys

def pikalang(str):
    str = str.lower()
    output = ''
    jsout = []
    for s in str:
        if s == 'a':
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            continue
        if s == 'b':
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'c':
            jsout.append('R')
            jsout.append('O')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'd':
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'e':
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'f':
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'g':
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'h':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'i':
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'j':
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'k':
            jsout.append('R')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'l':
            jsout.append('O')
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'm':
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'n':
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'o':
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'p':
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 'q':
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'r':
            jsout.append('O')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 's':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == 't':
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'u':
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'v':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'w':
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'x':
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'y':
            jsout.append('R')
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == 'z':
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == '0':
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == '1':
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == '2':
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == '3':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == '4':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('R')
            jsout.append('-')
            
            continue
        if s == '5':
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == '6':
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == '7':
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == '8':
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('O')
            jsout.append('-')
            
            continue
        if s == '9':
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('R')
            jsout.append('O')
            jsout.append('-')
            
            continue
        output += s
    return jsout

if __name__ == "__main__":
    if len(sys.argv) <= 1 or  len(sys.argv) >= 3:
        print("""invalid input.

If you want translate words, input:
python3 jsoreo.py nyanya
The Terminal will return:
app.oreoArr =  ['R', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'R', '-', 'R', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'R', '-']

Or translate sentence, input:
python3 jsoreo.py "Author by firedom"
The Terminal will return:
app.oreoArr =  ['O', 'R', '-', 'O', 'O', 'R', '-', 'R', '-', 'O', 'O', 'O', 'O', '-', 'R', 'R', 'R', '-', 'O', 'R', 'O', '-', 'R', 'O', 'O', 'O', '-', 'R', 'O', 'R', 'R', '-', 'O', 'O', 'R', 'O', '-', 'O', 'O', '-', 'O', 'R', 'O', '-', 'O', '-', 'R', 'O', 'O', '-', 'R', 'R', 'R', '-', 'R', 'R', '-']""")
        sys.exit(0)
    print('app.oreoArr = ' , pikalang(sys.argv[1]))
