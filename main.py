

numbers = []
while not any(num % 2 == 1 for num in numbers):
    x = int(input('number?'))
    numbers.append(x)

_is_odd = any(num % 2 == 1 for num in numbers)
