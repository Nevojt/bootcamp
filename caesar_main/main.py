from art import alphabet, logo
print(logo)
# Commit the changes
 
def caesar(start_text, shift_amount, cipher_direction):
    
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:    
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            
    print(f"The {cipher_direction}d text is {end_text}")

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    shift = shift % 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction= direction)
    cykl = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if cykl == "yes":
        flag = True
    elif cykl == "no":
        flag = False
        print("Goodbye!")
