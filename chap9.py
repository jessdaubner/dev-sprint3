# Name: Jessie Daubner
# Date: 11 February 2013
# Desc: Think Python Chapter 9 Exercises (9.1-9.4)

"""Exercise 9.1"""
def main():
	fin = open('words.txt')
	for line in fin:
		words = line.strip()
		if len(line) > 20:
			print words
		else:
			pass
main()


"""Exercise 9.2"""

def has_no_e(word):
	
	for letter in word:
		if letter == 'e': 
			return False
	return True
	

def print_list(l):
	for index in range(len(l)):
		print l[index]
	return ''

def main():
	total_words = 0	
	no_e_words = 0
	no_e_list = []
	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		total_words = total_words + 1

		if has_no_e(word):
			no_e_words = no_e_words + 1
			no_e_list.append(word) 

	percent = (no_e_words / float(total_words) * 100)
	print "These words in the file do not contain an 'e': ", print_list(no_e_list)
	print "The percent of the words in the file that do not contained an 'e' is ", percent
main()

"""Exercise 9.3"""

def avoids(word, forbidden):
	for letters in word:
		if letters in forbidden:
			return False
	return True

def print_list(l):
	for index in range(len(l)):
		print l[index]
	return ''

def main():
	total_words = 0	
	num_good_words = 0
	good_words =[]

	fin = open('words.txt')

	forbidden = raw_input("Enter the forbidden letters: ")

	for line in fin:
		word = line.strip()
		total_words = total_words + 1

		if avoids(word, forbidden):
			num_good_words = num_good_words + 1
			good_words.append(word) 

	bad_words = total_words - num_good_words
	print "These words in the file do not contain the forbidden letters: ", print_list(good_words)
	print "The number of words excluded with ", forbidden, "was", bad_words, "."

# jkqzx exclude 17,945 words

main()
	

"""Exercise 9.4"""

def uses_only(word, required):
	for letter in word:
		if letter not in required:
			return False
	return True

def print_list(l):
	for index in range(len(l)):
		print l[index]
	return ''

def main():
	required_words =[]

	fin = open('words.txt')

	required = raw_input("Enter the required letters: ")

	for line in fin:
		word = line.strip()

		if uses_only(word, required):
			required_words.append(word) 

	print "Can you make a sentence out of these words?", print_list(required_words)	
	
main()


