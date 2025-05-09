import sys
from stats import get_book_text, word_count, symbol_count, display_character_stats

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_total = word_count(book_path)
    char_counts = symbol_count(text)

    display_character_stats(char_counts, word_total, book_path)

if __name__ == "__main__":
    main()
