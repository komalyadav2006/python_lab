import sys

def caesar_cipher(text, shift, mode):
    result = ""

    if mode.lower() == "decode":
        shift = -shift

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result

if len(sys.argv) == 4:
    text = sys.argv[1]
    shift = int(sys.argv[2])
    mode = sys.argv[3]
else:
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    mode = input("Enter mode (encode/decode): ")

if mode.lower() not in ["encode", "decode"]:
    print("Invalid mode! Use 'encode' or 'decode'.")
else:
    output = caesar_cipher(text, shift, mode)
    print("Result:", output)