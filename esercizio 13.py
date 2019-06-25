def get_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fib(num - 1) + get_fib(num - 2)

num = int(input("Fino a che numero vuoi generare la stringa di Fibonacci? "))
print(get_fib(num))
