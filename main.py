from stats import word_count
from stats import get_book_text
from stats import symbol_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    
    words = word_count(book_path)
    print(f"{words} words found in the document")
    
    characters = symbol_count(book_text)
    print(characters)


main()