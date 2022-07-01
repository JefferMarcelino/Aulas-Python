def factorial(n):
    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1


def fibbonaci(n):
    if n >= 3:
        return fibbonaci(n - 1) + fibbonaci(n - 2)
    return 1

print(fibbonaci(4))