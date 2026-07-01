def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total

num = int(input("Enter a whole number: "))

print("Sum =", sum_of_numbers(num))