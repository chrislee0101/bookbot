import sys
from stats import get_num_words 
from stats import count_characters, sort_character_counts

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        return file_contents

def print_dict_values_combined(data_list):
    """
    Iterates through a list of dictionaries and prints the values 
    from each dictionary combined with a colon separator on a new line.
    """
    for item_dict in data_list:
        # Extract the values from the dictionary based on their known position
        char_value, num_value = item_dict.values() 
        
        # Use an f-string to combine the values with the required separator
        print(f"{char_value}: {num_value}")

#sys.argv = ['Usage: python3 main.py <path_to_book>',]
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
    else:    
        print("Too many arguments provided.")
        sys.exit(1)
    
    
    
    count = count_characters(book)
    #print(count)
    sorted_count = sort_character_counts(count)
        
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    get_num_words(book)
    print("--------- Character Count -------")
    print_dict_values_combined(sorted_count)
    print("============= END ===============")

    

main()
