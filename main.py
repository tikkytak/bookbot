from stats import word_count
from stats import character_count


with open('books/frankenstein.txt') as f:
        text = f.read()
            
            
def main():
        
        print(f"{word_count(text)} words found in the document")
        print(f"{character_count(text)}")
        

main()