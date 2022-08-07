from collections import Counter


def generate_phase(characters, phrase):
    if Counter(characters) == Counter(phrase):
        return phrase
    else:
        return ""


print(generate_phase("aabcdefa", "afeabcd"))
