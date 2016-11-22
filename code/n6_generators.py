def fib():
    nxt, current = 1, 0
    while True:
        nxt, current = nxt + current, nxt
        yield nxt


def odds(seq):
    for n in seq:
        if n % 2 == 1:
            yield n


for f in odds(fib()):
    if f > 1000:
        break
    print(f, end=', ')
