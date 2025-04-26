from stats import word_count
from stats import character_count
from stats import report

with open('books/frankenstein.txt') as f:
        text = f.read()
            
dict = character_count(text)            
def main():
        
        print(f"{report(dict)} words found in the document")       

main()