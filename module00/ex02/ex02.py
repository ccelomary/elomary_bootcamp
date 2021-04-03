from sys import argv

if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        num = int(argv[1])
        if not num:
            print ("I'm Zero.")
        elif num % 2:
            print ("I'm Odd.")
        else:
            print ("I'm Even.")
    else:
        print("ERROR.")