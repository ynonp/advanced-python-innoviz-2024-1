def sum_squares(*numbers):
    return sum(x*x for x in numbers)

numbers = [2, 3, 5]

print(sum_squares(2, 3, 5))
print(sum_squares(*numbers))
print(sum_squares(*range(10)))


