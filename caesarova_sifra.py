#zašifrovává a odšifrovává pomoci caesarovi šifry
import unicodedata
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def string_shift(text: str, key: int):
    result = ""
    text = text.upper()
    unicodedata.normalize("NFKD",text).encode("ascii","ignore").decode("ascii")
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65
            new_position = (position + key) % 26
            result += chr(new_position)
        else:
            continue
    return result

print(string_shift("Ahoj",3))
