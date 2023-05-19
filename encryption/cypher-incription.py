import random
import string
#https://www.youtube.com/watch?v=vsLBErLWBhA&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=30
#import char constants from the string module
chars = " " + string.punctuation + string.digits + string.ascii_letters
#typecast convert the string to a list
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"chars: {chars}")
print(f"key: {key}")


#encrypt

plain_text = input("Enter a message to encrypt")

cipher_text = ""

decypher_text = ""
#ENCYPHER
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Encrypted message:  " + cipher_text)

#DECYPHER

for letter in cipher_text:
    index = key.index(letter)
    decypher_text += chars[index]

print("Decrypted message:  " + decypher_text)



