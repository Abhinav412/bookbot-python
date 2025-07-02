def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    filepath = "/root/bookbot-python/books/frankenstein.txt"
    content = get_book_text(filepath)
    print(content)

if __name__ == "main":
    main()