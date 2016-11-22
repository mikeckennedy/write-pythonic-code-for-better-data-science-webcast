t = 1.2, 9.3, 87, .8

x, y, _, _ = t

# print(_)
print(x, y)

n = [1, 1, 2, 3, 5, 8, 12, 21]

for index, val in enumerate(n):
    print("{} --> {}".format(index, val))

print(x, y)
y, x = x, y
print(x, y)
