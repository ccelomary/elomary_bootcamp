

def     text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""

    upper_case = 0
    lower_case = 0
    punct = 0
    space = 0
    if (len(args) > 1):
            print("ERROR")
            return
    text = args[0]
    if not text:
        print("What is the text to analyse?")
        input(">> ")
    for letter in text:
        if letter.islower():
            lower_case += 1
        elif letter.isupper():
            upper_case += 1
        elif letter.isspace():
            space += 1
        elif not letter.isalnum():
            punct += 1
    print("The text contains {} characters:".format(len(text)))
    print("- {} upper letters".format(upper_case))
    print("- {} lower letters".format(lower_case))
    print("- {} punctuation marks".format(punct))
    print("- {} spaces".format(space))
