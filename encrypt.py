import string


key = input("Enter the key: \t").upper()
alphabets = string.ascii_uppercase   # get all the abcd's
values = [i for i in range(26)]   # 0-25 values representing abcd's
shifts = [alphabets.index(i) for i in key]   # the shifts of the keys
last_shift = 0

with open("plain_text.txt", "r") as read:
	plain_text = read.readlines()


for i, sent in enumerate(plain_text):
	plain_text[i] = "".join(i.upper() for i in sent if i.isalpha() or i == " ")

encrypted_text = []

for text in plain_text:
	x = ""   # encrypted sentence

	for character in text:

		if character in alphabets:   # encrypt the word
			index = alphabets.index(character) + shifts[last_shift]

			if last_shift == len(shifts) - 1:

				if index > 25:    # if the index of the encrypted alphabet is greater than the table, continue from the beginning
					index -= 26

				x += alphabets[index]
				# print(index, alphabets.index(character) + shifts[last_shift], character, alphabets.index(character), shifts[last_shift])
				last_shift = 0

			else:

				if index > 25:   # if the index of the encrypted alphabet is greater than the table, continue from the beginning
					index -= 26

				x += alphabets[index]
				# print(index, alphabets.index(character) + shifts[last_shift], character, alphabets.index(character), shifts[last_shift])
				last_shift += 1

		else:   # space b/w words, commas, full stops is defined by +
			x += "+"

	x += "\n"
	encrypted_text.append(x)

with open("encrypted_text.txt", "w") as write:
	write.writelines(encrypted_text)
