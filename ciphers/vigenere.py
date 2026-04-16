UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"


def _clean_key(key):
    letters = [char for char in str(key) if char.isalpha()]
    if not letters:
        raise ValueError("Key must contain at least one letter.")
    return "".join(letters)


def _key_shifts(text, key):
    clean_key = _clean_key(key)
    index = 0
    for char in text:
        if char.isalpha():
            yield clean_key[index % len(clean_key)].lower(), char
            index += 1
        else:
            yield None, char


def _translate_traditional(char, key_char, direction):
    if not key_char:
        return char

    shift = LOWERCASE.index(key_char) * direction
    alphabet = UPPERCASE if char.isupper() else LOWERCASE
    position = alphabet.index(char)
    return alphabet[(position + shift) % 26]


def _translate_math(char, key_char, direction):
    if not key_char:
        return char

    shift = (ord(key_char) - ord("a")) * direction
    base = ord("A") if char.isupper() else ord("a")
    return chr((ord(char) - base + shift) % 26 + base)


def _transform(text, key, translator, direction):
    return "".join(
        translator(char, key_char, direction)
        for key_char, char in _key_shifts(text, key)
    )


def encrypt_traditional(text, key):
    return _transform(text, key, _translate_traditional, 1)


def decrypt_traditional(text, key):
    return _transform(text, key, _translate_traditional, -1)


def encrypt_math(text, key):
    return _transform(text, key, _translate_math, 1)


def decrypt_math(text, key):
    return _transform(text, key, _translate_math, -1)
