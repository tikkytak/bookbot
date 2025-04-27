from stats import word_count
from stats import character_count
from stats import sort
import sys



         
def main():
        
        if len(sys.argv) < 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
                
        else:
                with open(sys.argv[1]) as f:
                        text = f.read()
            
                dict = character_count(text)   

                sorted_list = sort(dict)       
                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {sys.argv[1]}")
                print("----------- Word Count ----------")
                print(f"Found {word_count(text)} total words")
                print("--------- Character Count -------")
                for dictionary in sorted_list:
                        if dictionary["char"].isalpha():
                                print(f"{dictionary["char"]}: {dictionary["num"]}")
                print("============= END ===============")

main()