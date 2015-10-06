def ceasar(text, key):
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	enc = list(alphabet[key:]+alphabet[0:key])
	ans = ""

	for letter in text:
		idx = alphabet.index(letter)
		ans += enc[idx]

	print("Encrypted text:\n" + ans)

text = input("Input text to be encrypted:\n").lower()
key = int(input("Encryption key:\n"))

ceasar(text, key)
