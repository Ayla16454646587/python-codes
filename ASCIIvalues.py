char=input("Enter a character")

if len(char) !=1:
    print("Enter exactly ONE character")
else:
    ascii_value=ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")