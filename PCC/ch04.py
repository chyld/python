odds = range(1, 20, 2)
for idx, val in enumerate(odds):
    print("index:{}; value:{}".format(idx, val))

even_squares = [x**2 for x in range(25) if x % 2 == 0]
print('even_squares:', even_squares)

small_squares = even_squares[:5]
print('small_squares:', small_squares)

evens = tuple((x, x**2) for x in range(3, 30) if x % 3 == 0)
print('evens:', evens)
