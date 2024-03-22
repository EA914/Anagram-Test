def are_anagrams(str1, str2):
	if len(str1) != len(str2):
		return False
	
	char_freq = {}
	for char in str1:
		if char in char_freq:
			char_freq[char] += 1
		else:
			char_freq[char] = 1

	for char in str2:
		if char in char_freq:
			char_freq[char] -= 1
		else:
			return False

	for freq in char_freq.values():
		if freq != 0:
			return False
	
	return True

str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

if are_anagrams(str1, str2):
	print(f"'{str1}' and '{str2}' are anagrams of each other.")
else:
	print(f"'{str1}' and '{str2}' are NOT anagrams of each other.")