import os, sys

def pikalang(str):
    str = str.lower()
    output = ''
    for s in str:
        if s == 'a':
            output += '奥利与'
            continue
        if s == 'b':
            output += '利奥奥奥与'
            continue
        if s == 'c':
            output += '利奥里奥与'
            continue
        if s == 'd':
            output += '利奥奥与'
            continue
        if s == 'e':
            output += '奥与'
            continue
        if s == 'f':
            output += '奥奥利奥与'
            continue
        if s == 'g':
            output += '利利奥与'
            continue
        if s == 'h':
            output += '奥奥奥奥与'
            continue
        if s == 'i':
            output += '奥奥与'
            continue
        if s == 'j':
            output += '奥利利利与'
            continue
        if s == 'k':
            output += '利奥利与'
            continue
        if s == 'l':
            output += '奥利奥奥与'
            continue
        if s == 'm':
            output += '利利与'
            continue
        if s == 'n':
            output += '利奥与'
            continue
        if s == 'o':
            output += '利利利与'
            continue
        if s == 'p':
            output += '奥利利奥与'
            continue
        if s == 'q':
            output += '利利奥利与'
            continue
        if s == 'r':
            output += '奥利奥与'
            continue
        if s == 's':
            output += '奥奥奥与'
            continue
        if s == 't':
            output += '利与'
            continue
        if s == 'u':
            output += '奥奥利与'
            continue
        if s == 'v':
            output += '奥奥奥利与'
            continue
        if s == 'w':
            output += '奥利利与'
            continue
        if s == 'x':
            output += '利奥奥利与'
            continue
        if s == 'y':
            output += '利奥利利与'
            continue
        if s == 'z':
            output += '利利奥奥与'
            continue
        if s == '0':
            output += '利利利利利与'
            continue
        if s == '1':
            output += '奥利利利利与'
            continue
        if s == '2':
            output += '奥奥利利利与'
            continue
        if s == '3':
            output += '奥奥奥利利与'
            continue
        if s == '4':
            output += '奥奥奥奥利与'
            continue
        if s == '5':
            output += '奥奥奥奥奥与'
            continue
        if s == '6':
            output += '利奥奥奥奥与'
            continue
        if s == '7':
            output += '利利奥奥奥与'
            continue
        if s == '8':
            output += '利利利奥奥与'
            continue
        if s == '9':
            output += '利利利利奥与'
            continue
        output += s

    return output

if __name__ == "__main__":
    if len(sys.argv) <= 1 or  len(sys.argv) >= 3:
        print("""invalid input.

If you want translate words, input:
python3 tapcode.py nyanya~
The Terminal will return:
· ··与· ·· · ·与·· ·与· ··与· ·· · ·与·· ·与~

Or translate sentence, input:
python3 tapcode.py "Author by firedom"
The Terminal will return:
·· ·与··· ·与· ·与·····与· · · ·与·· ··与 与· ····与· ·· · ·与 与··· ··与···与·· ··与··与· ···与· · · ·与· · ·与""")
        sys.exit(0)
    print(pikalang(sys.argv[1]))
