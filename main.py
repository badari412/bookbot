def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f'--- Begin report of {book_path} ---')
    print(f"{num_words} words found in the document")
    num_letters_dict = get_no_of_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_letters_dict)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sorted_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sorted_on)
    return sorted_list

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_no_of_letters(text):
    res = {}
    for letter in text.lower():
        if not letter.isalpha():
            continue
        if not letter in res:
            res[letter] = 1
        else:
            res[letter] += 1
    return res

main()