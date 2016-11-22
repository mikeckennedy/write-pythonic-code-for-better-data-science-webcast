def filter_numbers(test):
    data = []
    for n in range(50):
        if test(n):
            data.append(n)

    return data


evens = filter_numbers(lambda x: x % 2 == 0)
print(evens)

data = [1, 9, -1, 20, 5, -100]
data.sort(key=lambda x: abs(x))

print(data)