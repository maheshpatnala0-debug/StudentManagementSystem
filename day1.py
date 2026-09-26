number = input("Enter a number: ")

reverse = ""

for digit in number:
    reverse = digit + reverse

print("Reverse:", reverse)