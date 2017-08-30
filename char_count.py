"""
Code for counting number of characters in a sentence.

"""

sentence = input("Enter a sentence here : ")
sentence = sentence.lower()

words = list(sentence)

count_words = {}

for word in words:
	characters = list(word)
	for char in characters:
		if char in count_words:
			count_words[char] += 1
		else:
			count_words[char] = 1
sorted_keys = sorted(count_words.keys())
for k in sorted_keys:
	v = count_words[k]
	print("Found :  {0} : {1}".format(k,v))