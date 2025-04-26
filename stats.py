def word_count(text):
        words = text.split()
        return len(words)

def character_count(text):
        characters = {}
        text = text.lower()
        for char in text:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1    
        return characters 

def report(dict):
    list = []
    for key in dict:
        if key.isalpha() == True:
             list.extend(dict.items())
             
    return list