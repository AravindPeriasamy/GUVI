character = input()
vowels = ['a','e','i','o','u']
if character.isalpha():
	if character.lower() in vowels:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
