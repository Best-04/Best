def shift_letter(letter,shift):
    return chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))

text = input("Enter the plain text = ")
shift = int(input("Enter the shift value = "))

shifted_text = "" 

for letter in text:
    if letter.isalpha():  
        shifted_text += shift_letter(letter, shift)
    else:
        shifted_text += letter  

print("Shifted text:", shifted_text)   


