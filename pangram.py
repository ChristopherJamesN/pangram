def is_pangram(sentence):
    all_characters = 'abcdefghijklmnopqrstuvwxyz'
    for value in all_characters:
        if not checkcharacter(value, sentence):
            return False
    return True

def checkcharacter(character, sentence):
    if character in str(sentence.lower()):
        return True
    else:
        return False
