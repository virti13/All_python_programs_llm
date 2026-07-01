try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    else:
        print("Your age is", age)

except ValueError:
    print("Invalid input! Please enter a valid number.")