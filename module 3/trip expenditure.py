def trip_expenditure(travel, food, hotel, shopping):
    return travel + food + hotel + shopping

travel = float(input("Enter travel expense: "))
food = float(input("Enter food expense: "))
hotel = float(input("Enter hotel expense: "))
shopping = float(input("Enter shopping expense: "))

total = trip_expenditure(travel, food, hotel, shopping)

print("Total Trip Expenditure =", total)