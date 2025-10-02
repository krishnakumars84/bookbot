
import sys
from stats import get_word_count, character_counter, generate_sorted_report_from_dict

def get_book_text(file_path: str):
    if not file_path: 
        raise
    print(f"Analyzing book found at {file_path}...")
    with open(file_path) as book:
        book_text = book.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    print("============ BOOKBOT ============")
    book_text = get_book_text(file_path=sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    book_char_count = character_counter(book_text)
    sorted_report = generate_sorted_report_from_dict(book_char_count)
    for item in sorted_report: 
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


main()