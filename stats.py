
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

def display_character_stats(char_counts, word_count, book_path):
    print("====================== BOOKBOT ======================")
    print(f"Analyzing book found at {book_path}...")
    print("--------------------- Word Count --------------------")
    print(f"Found {word_count} total words")
    print("------------------- Character Count -----------------")
    
    sorted_counts = sorted(
        ((char, count) for char, count in char_counts.items() if char.isalpha()),
        key=lambda item: item[1],
        reverse=True
    )

    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("======================= END =========================")


