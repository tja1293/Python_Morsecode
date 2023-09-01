# Name: Thomas Alsop
# A Morse code encoder/decoder

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
              'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
              ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
              }


def print_intro():
    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")


def get_input():
    choice = input("Would you like to encode (e) or decode (d): ")
    encodes = choice == "e"
    while choice != "e" and choice != "d":
        print("Invalid Mode")
        choice = input("Would you like to encode (e) or decode (d): ")
    if encodes:
        message = input("What would you like to encode? ")
    else:
        message = input("What would you like to decode? ")
    return choice, message


def encode(message):
    secret_message = " "
    for i in message:
        if i != " ":
            secret_message += MORSE_CODE[i] + " "
        else:
            secret_message += " "
    return secret_message


def main():
    print_intro()
    choice, message = get_input()
    result = encode(message.upper())
    print(result)
    print(message)

    yes_no = input("Would you like to encode/decode another message? (y/n) ")
    while yes_no != "y" and yes_no != "n":
        yes_no = input("Would you like to encode/decode another message? (y/n) ")
    if yes_no == "y":
        get_input()
    else:
        print("Thanks for using the program, goodbye!")


if __name__ == '__main__':
    main()
