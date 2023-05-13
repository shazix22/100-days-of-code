print("Welcome to the tip calculator!")
print("What was the total bill?")
x = int(input())
print("How man people to split the bill?")
y = int(input())
print("What percentage tip would you like to give? 10, 12, 15?")
z = float(input())
print()

calc = x * (1 + (z/100)) / y

print("final",calc)