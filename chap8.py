# Name: Jessie Daubner
# Date: 9 February 2013
# Desc: create a function that imitates ROT13 encryption


def rotate_word(str, int):
	rotated_words = ''
	for j in range(len(str)):
		character = str[j]
		code = ord(character)
		if code == 32:
			new_code = code
		elif code >= 110:
			new_code = 97 + (code - 110)
		elif (code >= 78) and (code <= 90):
			new_code = 65 + (code - 78)
		else:	
			new_code = code + 13
		new_chr = chr(new_code)
		rotated_words = rotated_words + new_chr
	return rotated_words


def main():
	sentence = raw_input("Enter a sentence to encrypt: ")
	encryption = rotate_word(sentence, 13)
	print ("Your encrypted sentence is: " + '\n' + encryption)
main()