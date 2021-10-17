import string


key = input("Enter the key: \t").upper()
alphabets = string.ascii_uppercase   # get all the abcd's
values = [i for i in range(26)]   # 0-25 values representing abcd's
shifts = [alphabets.index(i) for i in key]   # the shifts of the keys
last_shift = 0

with open("encrypted_text.txt", "r") as read:
	encrypted_text = read.readlines()

encrypted_text = [i[:-1].upper() for i in encrypted_text if i!=""]
decrypted_text = []

for text in encrypted_text:
	x = ""   # decrypted sentence

	for character in text:
		
		if character in alphabets:
			index = alphabets.index(character) - shifts[last_shift]

			if index < 0:
				index = 26 - abs(index)

			x += alphabets[index]

			if last_shift == len(shifts) - 1:
				last_shift = 0

			else:
				last_shift += 1


		else:
			x += " "

	x += "\n"
	decrypted_text.append(x)

with open("decrypted_text.txt", "w") as write:
	write.writelines(decrypted_text)
