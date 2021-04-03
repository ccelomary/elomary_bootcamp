from sys import argv

def usage():
    print("""Usage: python operations.py <number1> <number2>
Example:
        python operations.py 10 3""")
    

if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    elif len(argv) > 3:
        print("InputError: too many arguments")
        usage()
    elif not all((number.isdigit() for number in argv[1:])):
        print("InputError: only numbers")
        usage()
    else:
        a = int (argv[1])
        b = int (argv[2])
        print("Sum:         {}".format(a + b))
        print("Difference:  {}".format(a - b))
        print("Product:     {}".format(a * b))
        print("Quotient:    {}".format(a / b if b else "ERROR (div by zero)"))
        print("Remainder:   {}".format(a % b if b else "ERROR (modulo by zero)"))
