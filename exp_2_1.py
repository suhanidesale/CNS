encrypted_message = "hcdsjch"

stored_letters = {}

for char in encrypted_message:
    if char not in stored_letters:
     stored_letters[char] = 1
    else:
     stored_letters[char] +=1
    
print(stored_letters)

  