import sys

from stats import get_char_map, get_ind_dicts, get_num_words



def main(filepath):
    num_words = get_num_words(filepath)
    # print(f'{num_words} words found in the document')
    res = get_ind_dicts(get_char_map(filepath))
    # print(res)
    
    char_map_string = ""
    for indmap in res:
        if indmap["char"].isalpha() == False:
            continue        
        char_map_string += f"{indmap['char']}: {indmap['num']}\n"
    
    report = f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_map_string}============= END ==============="""
    print(report)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])

