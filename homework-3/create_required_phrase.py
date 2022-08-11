from collections import Counter


def generate_phase(characters, phrase):
    try:
        if Counter(characters) == Counter(phrase):
            return True
        else:
            return False
    except:
        return ""



print(generate_phase("aabcdefa", "afeabcd"))
