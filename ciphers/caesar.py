UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"


def _normalize_shift(shift):
    return int(shift) % 26


def _shift_from_alphabet(char, shift, alphabet):
    index = alphabet.index(char)
    return alphabet[(index + shift) % 26]


def _translate_traditional(char, shift):
    if char in UPPERCASE:
        return _shift_from_alphabet(char, shift, UPPERCASE)
    if char in LOWERCASE:
        return _shift_from_alphabet(char, shift, LOWERCASE)
    return char


def _translate_math(char, shift):
    if "A" <= char <= "Z":
        base = ord("A")
    elif "a" <= char <= "z":
        base = ord("a")
    else:
        return char
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt_traditional(text, shift):
    shift = _normalize_shift(shift)
    return "".join(_translate_traditional(char, shift) for char in text)


def decrypt_traditional(text, shift):
    return encrypt_traditional(text, -int(shift))


def encrypt_math(text, shift):
    shift = _normalize_shift(shift)
    return "".join(_translate_math(char, shift) for char in text)


def decrypt_math(text, shift):
    return encrypt_math(text, -int(shift))


def brute_force(text):
    return "\n".join(f"Shift {shift}: {decrypt_math(text, shift)}" for shift in range(26))
