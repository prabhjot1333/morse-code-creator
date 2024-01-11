# morse code creator

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


# convert to morse code
def to_encode(message):
    encode_code = ""
    for letter in message:
        if letter in MORSE_CODE_DICT:
            encode_code += MORSE_CODE_DICT[letter] + " "
    print(encode_code)
    return encode_code


# convert back to text
def to_decode(coded_message):
    plain_text = ""
    coded_message = coded_message.split(' ')
    for code in coded_message:
        for key, value in MORSE_CODE_DICT.items():
            if value == code:
                plain_text += key
    print(plain_text)
    return plain_text


CODING = True

while CODING:
    display_message = "Type 1: to code.\n Type 2: to decode.\n Type 3: to exit."
    print(display_message)
    choice = input("Chose an option.")
    if choice == '1':
        text_to_code = input("Please write what you want coded:\n").upper()
        to_encode(message=text_to_code)
    elif choice == '2':
        code_to_text = input("Please write the code to be decoded:\n")
        to_decode(coded_message=code_to_text)
    elif choice == '3':
        print("U exited")
        CODING = False
    else:
        print("Your entry is invalid.")
