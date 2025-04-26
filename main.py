from stats import word_count
from stats import character_count
from stats import sort

with open('books/frankenstein.txt') as f:
        text = f.read()
            
dict = character_count(text)            
def main():
        
        sorted_list = sort(dict)       
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(text)} total words")
        print("--------- Character Count -------")
        for dictionary in sorted_list:
                if dictionary["char"].isalpha():
                        print(f"{dictionary["char"]}: {dictionary["num"]}")
        print("============= END ===============")

main()