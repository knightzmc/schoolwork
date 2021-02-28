alphabet = "abcdefghijklmnopqrstuvwxyz !.,"


def caesar(text, n):
    return ''.join([alphabet[(alphabet.find(c.lower()) + n) % len(alphabet)].capitalize() if c.isupper() else alphabet[
        (alphabet.find(c) + n) % len(alphabet)] for c in text])


def caesar_decrypt(text, n):
    return caesar(text, -n)


output = caesar('Hello!', 3)
print(caesar_decrypt(output, 3))
