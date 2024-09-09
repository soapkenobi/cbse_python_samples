terms = int(input())
fib = [0, 1]
for i in range(2, terms):
    fib.append(fib[i-1] + fib[i-2])
for i in fib:
    print(i, end = ' ' if i != fib[len(fib) - 1] else '\n')
