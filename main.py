from stats import text_count,get_chars_dict,chars_to_list

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def print_report(book_path,num_words,chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    filepath = "books/frankenstein.txt"
    content = get_book_text(filepath)
    num_words = text_count(content)
    chars_dict = get_chars_dict(content)
    chars_list = chars_to_list(chars_dict)
    print_report(filepath,num_words,chars_list)

if __name__ == "__main__":
    main()