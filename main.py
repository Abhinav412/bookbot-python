from stats import text_count

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    filepath = "/root/bookbot-python/books/frankenstein.txt"
    content = get_book_text(filepath)
    num_words = text_count(content)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()