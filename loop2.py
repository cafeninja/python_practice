my_numbers = [1, 2, 3]
my_square_numbers = []

for number in my_numbers:
    my_square_numbers.append(number**2)

print(f"The list of numbers: {my_numbers}")
print(f"The list of squares: {my_square_numbers}")

even_numbers = []
odd_numbers = []
for number in my_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)




for square in my_square_numbers:
    if square % 2 == 0:
        even_numbers.append(square)
    else:
        odd_numbers.append(square)

even_numbers = list(dict.fromkeys(even_numbers))
odd_numbers = list(dict.fromkeys(odd_numbers))

print(f"List of even numbers and squares: {even_numbers}")
print(f"List of odd numbers and squares: {odd_numbers}")

