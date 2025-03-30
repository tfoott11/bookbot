import sys
from stats import count_words
from stats import char_count
from stats import sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1] 

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	frank=get_book_text(book_path)
	count=count_words(frank)
	char_counts = char_count(frank)
	sorted_chars= sort_chars(char_counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}" )
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for char_dict in sorted_chars:
		char = char_dict["char"]
		count = char_dict["count"]
		if char.isalpha():
			print (f"{char}: {count}")

	print("============= END ===============")
main()
