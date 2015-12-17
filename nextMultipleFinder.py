# This program is for choosing the next multiple of a given divisor.

# Choose divisor.
divisor = input('Enter divisor to set as base (e.g. 5, 25, 50 or anything): ')

# Input a number.
number = input('Enter a number to find the next multiple: ')

# def multipleCheck(number, divisor):

# If not directly divisible by divisor.
if number % divisor != 0:
    y = int(number / divisor)       # flooring the value.
    y += 1                          # Adding 1 for choosing next multiple.
    final_value = y * divisor       # Multiply the new quotient with divisor.

elif number == 0:
    final_value = divisor

else:
    final_value = number

print final_value
