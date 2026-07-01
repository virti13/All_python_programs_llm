age = int(input("Enter your age: "))

if age >= 0:
    if age < 13:
        print("You are a Child.")
    else:
        if age < 20:
            print("You are a Teenager.")
        else:
            if age < 60:
                print("You are an Adult.")
            else:
                print("You are a Senior Citizen.")
else:
    print("Invalid age entered.")