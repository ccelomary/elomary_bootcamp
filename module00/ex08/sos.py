from sys import argv
import re
MORSE_CODE = {'..--..': '?', '-.--': 'Y', '...-..-': '$', '---': 'O', '--..--': ',', '.-': 'A',
'.-..-.': '"', '.': 'E', '.-..': 'L', '-...': 'B', '...': 'S', '.-.': 'R', '---..': '8', '..-.': 'F',
'-----': '0', '.----': '1', '--...': '7', '-.-.': 'C', '..-': 'U', '.--.': 'P', '...--': '3', '----.': '9',
'..---': '2', '....': 'H', '.--.-.': '@', '--': 'M', '.-.-.': '+', '...---...': 'SOS', '-..': 'D', '....-': '4',
'..': 'I', '-...-': '=', '.----.': "'", '-..-.': '/', '-': 'T', '.....': '5', '.-.-.-': '.', '--..': 'Z', '--.-': 'Q',
'-....-': '-', '-.--.': '(', '...-': 'V', '..--.-': '_', '-..-': 'X',
'--.': 'G', '.---': 'J', '.-...': '&', '-.': 'N', '---...': ':', '-.--.-': ')',
'.--': 'W', '-.-': 'K', '-....': '6', '-.-.--': '!', '-.-.-.': ';'}

MORSE_CODE = dict(zip(MORSE_CODE.values(), MORSE_CODE.keys()))

if __name__ == '__main__':
    if len(argv) < 2:
        print("ERROR")
    else:
        if not all(re.match(r"^[0-9A-Za-z\s]+$", s) for s in argv[1:]):
            print('ERROR')
        else:
            print(" / ".join([''.join([MORSE_CODE.get(c.upper(),
                ' / ') for c in arg]) for arg in argv[1:]]))
        