# Problem Statement:
# The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.
# It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter
# some fixed number of positions down the alphabet.
# For example with a shift of 1, A would be replaced by B, B would become C, and so on.
# The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
# Thus to cipher a given text we need an integer value, known as shift
# which indicates the number of position each letter of the text has been moved down.
# The encryption can be represented using modular arithmetic by first transforming the letters into numbers,
# according to the scheme, A = 0, B = 1,…, Z = 25.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodby")