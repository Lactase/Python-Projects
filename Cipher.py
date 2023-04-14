def caesar_cipher (string, shift = 1):
    # Creates a new string
    new_string = ""
    # Special Characters
    special_char = "[@_!#$%^&*()<>?/\|}{~:.], "
    # Stops the function from running if it is not a string or it is blank
    if (type(string) != str or string == ""):
       return print("Enter a string")
    # Loops through characters
    for i in range(len(string)):
        # If it is a special character it ignores it and adds it to the new string
        if (string[i] in special_char):
            new_string += string[i]
            continue
        # If Uppercase characters shift beyond Z it loops back to beginning
        if (string[i].isupper() and (ord(string[i]) + shift > 90 )):
            new_string += (chr(64 + (ord(string[i]) + shift) - 90 ))
        # If Lowercase characters shift beyond z it loops back to beginning
        elif (string[i].islower() and (ord(string[i]) + shift > 122 )):
            new_string += (chr(96 + (ord(string[i]) + shift) - 122 ))
        # If not, it adds shift to the character
        else:
            new_string +=(chr(ord(string[i]) + shift))
        
    # Returns and prints the new string
    return print(new_string)

caesar_cipher("Hello, World!", 25)




