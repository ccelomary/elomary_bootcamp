from sys import argv
import string
import re
if __name__ == '__main__':
    if len(argv) != 3:
        print("ERROR")
    else:
        if argv[1].isdigit():
            print("ERROR")
        elif not argv[2].isdigit():
            print("ERROR")
        else:
            s = re.sub(r'[!"#\$%&\'()\*\+,-./:;<=>\?@\[\\\]^_`{|}~]+', " ", argv[1])
            l = int(argv[2])
            print([word for word in s.split(" ") if len(word) > l])

