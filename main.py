from stats import text_count,get_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    filepath = "books/frankenstein.txt"
    content = get_book_text(filepath)
    num_words = text_count(content)
    chars_dict = get_chars_dict(content)
    print(f"{num_words} words found in the document")
    print(chars_dict)

if __name__ == "__main__":
    main()