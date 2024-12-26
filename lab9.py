def square(num, print_result=False):
    result = num ** 2
    if print_result:
        print(f"Квадрат числа равен: {result}")
        return
    return result

print(square(4))
square(5, print_result=True)
square(6, print_result=True)
