import random
from string import *


characters = " " + digits + punctuation + ascii_letters
characters = list(characters)
print(characters)
key = characters[:]
random.shuffle(key)
print(key)

sentence_to_encrypt = input("What do you want to encrypt: ")
cipher_sentence = []
plain_sentence = []
for letters in sentence_to_encrypt:
    index = characters.index(letters)
    new_letter = key[index]
    cipher_sentence.append(new_letter)

print("This is your encrypted sentence:")
for letters in cipher_sentence:
    print(letters, end="")


sentence_to_decrypt = input("\nEnter what you want to decrypt: ")
for letters in sentence_to_decrypt:
    index = key.index(letters)
    new_letter = characters[index]
    plain_sentence.append(new_letter)


print("This is your decrypted sentence:")
for letters in plain_sentence:
    print(letters, end="")



