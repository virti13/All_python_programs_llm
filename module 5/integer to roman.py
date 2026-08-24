num = int(input("Enter a number: "))

values = [100, 50, 10, 5, 1]
symbols = ["C", "L", "X", "V", "I"]

roman = ""

for i in range(len(values)):
    while num >= values[i]:
        roman = roman + symbols[i]
        num = num - values[i]

print("Roman number:", roman)