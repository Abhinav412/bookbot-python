def text_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_to_list(char_dict):
    sorted = []
    for ch in char_dict:
        sorted.append({"char":ch,"num":char_dict[ch]})
    sorted.sort(reverse=True,key=sort_on)
    return sorted