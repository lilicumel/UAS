# affine_cipher.py
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, key_a, key_b):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((key_a * (ord(char) - ord('A')) + key_b) % 26 + ord('A'))
            else:
                result += chr((key_a * (ord(char) - ord('a')) + key_b) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(text, key_a, key_b):
    result = ""
    key_a_inv = mod_inverse(key_a, 26)
    if key_a_inv is not None:
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((key_a_inv * (ord(char) - ord('A') - key_b)) % 26 + ord('A'))
                else:
                    result += chr((key_a_inv * (ord(char) - ord('a') - key_b)) % 26 + ord('a'))
            else:
                result += char
    return result
