
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(book):
    full_book = get_book_text(book)
    words = len(full_book.split())
    return words

def symbol_count(text):
    symbol = {}
    for char in text.lower():
        if char in symbol:
            symbol[char] += 1
        else: symbol[char] = 1
    return symbol