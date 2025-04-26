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

def sort_on(dict):
     return dict["num"]

def sort(dict):
    result = []
    for char, count in dict.items():
        char_dict = {"char": char, "num":count}
        result.append(char_dict)

    result.sort(reverse=True, key=sort_on)    
    return result