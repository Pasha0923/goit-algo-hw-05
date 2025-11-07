# функція caching_fibonacci створює внутрішню функцію fibonacci, яка обчислює n-е число Фібоначчі. Використовується словник cache для збереження вже обчислених значень, що дозволяє уникнути повторних обчислень і значно покращує продуктивність.
def caching_fibonacci():
    """Функція для обчислення n-го числа Фібоначчі з використанням кешування"""
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(15)) # 610 

