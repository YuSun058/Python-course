def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


# Press 'F5' to reach the break point, press 'Shift+F5' to jump out of the debugging
print("Start debugging")  # Press 'F10' to run line by line
# Press 'F11' to go into the function, and press 'Shift+F11' to jump out of that function
print(multiply(2, 3, 4))
