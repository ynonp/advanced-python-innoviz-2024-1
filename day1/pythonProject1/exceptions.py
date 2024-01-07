"""
Exceptions are a way to control program flow
"""

class EncryptionError(Exception):
    pass

def encrypt(secret_message):
    if secret_message == "hello":
        return "$$$$$$"
    else:
        raise EncryptionError(f"Don't know how to encrypt {secret_message}")

reverse = {
    "one": "eno",
    "two": "owt",
    "three": "eerht"
}

try:
    text = input("select a number").strip()
    text_to_encrypt = reverse[text]
    print(encrypt(text_to_encrypt))
except KeyError:
    print("Can only use numbers: one, two and three")
except EncryptionError:
    print("Can only encrypt text hello")




