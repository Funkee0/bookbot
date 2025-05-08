from stats import get_book_text, symbol_count, display_character_stats

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    word_count = len(text.split())
    char_counts = symbol_count(text)

    display_character_stats(char_counts, word_count)

main()