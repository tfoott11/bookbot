def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
	count={}
	for char in text:
		char = char.lower()
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	return count
def sort_chars(char_dict):
	char_list=[]
	for char, count in char_dict.items():
		char_list.append({"char": char, "count": count})
	def sort_on(dict):
		return dict["count"]
	char_list.sort(reverse=True, key= sort_on)
	return char_list
