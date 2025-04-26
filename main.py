from stats import word_count
from stats import character_count
from stats import sort

with open('books/frankenstein.txt') as f:
        text = f.read()
            
dict = character_count(text)            
def main():
        
        sorted_list = sort(text)       

main()