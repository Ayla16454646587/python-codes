while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)  
        print(f"your age is: {number}")
        break  
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")