def caesar_cipher (string, shift = 1):
    new_string = ""
    special_char = "[@_!#$%^&*()<>?/\|}{~:.], "
    if (type(string) != str or string == ""):
       return print("Enter a string")
    
    for i in range(len(string)):
        if (string[i] in special_char):
            new_string += string[i]
            continue
        if (string[i].isupper() and (ord(string[i]) + shift > 90 )):
            new_string += (chr(64 + (ord(string[i]) + shift) - 90 ))
        elif (string[i].islower() and (ord(string[i]) + shift > 122 )):
            new_string += (chr(96 + (ord(string[i]) + shift) - 122 ))
        else:
            new_string +=(chr(ord(string[i]) + shift))
        
    
    return print(new_string)

caesar_cipher("Hello, World!", 25)




