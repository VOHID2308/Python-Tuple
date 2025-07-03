numbers = (3, 6, 7, 8, 10, 11)

new_tuple = ()

for number in numbers:
    if number % 2 == 0:
        new_tuple += (number,)

print(new_tuple)