from sys import  argv

if __name__ == '__main__':
    if len(argv) > 1:
        l = " ".join(argv[1:])
        l = "".join([i.upper() if i.islower() else i.lower() for i in l])
        print(l[::-1])