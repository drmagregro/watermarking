import string

def cesar_cipher(text, key, cipher):
	if type(text) == str and type(key) == int:
		shift = 1 if cipher else -1
		list_of_crypted_chars = []
		for char in text :
			list_of_crypted_chars.append(chr((ord(char) + shift * key) % 1_114_112))

		crypted_text = "".join(list_of_crypted_chars)
		return crypted_text
	else:
		raise(TypeError)


def vigenere_cipher(text, password, cipher):
	list_of_crypted_chars = []
	list_of_keys = [ord(char) for char in password]
	
	for index, current_char in enumerate(text):
		
		current_key = list_of_keys[index % len(list_of_keys)]
		current_crypted_char = cesar_cipher(current_char, current_key, cipher)

		list_of_crypted_chars.append(current_crypted_char)

	crypted_text = "".join(list_of_crypted_chars)

	return crypted_text