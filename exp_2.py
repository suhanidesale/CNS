most_used = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 
'x', 'q', 'z']

cipher =  'iwooxqjgbknhaypnaopkzwu'

occurence = {}

for symbol in cipher:
    if symbol in occurence:
        occurence[symbol] += 1
    else:
        occurence[symbol] = 1

print(occurence)


def decrypt(cipher, k):
    plain_text = ""
    for symbol in cipher:
        pt = (ord(symbol) - 97 - k)%26
        pt = chr(pt+97)
        plain_text += "".join(pt)
    print(f"{letter}; PlainText: {plain_text}")

word = max(occurence, key=occurence.get)
print(word)

for letter in most_used:
    k = (ord(word) - ord(letter))%26
    decrypt(cipher, k)