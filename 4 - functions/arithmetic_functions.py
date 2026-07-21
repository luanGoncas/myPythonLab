def plus_one(number): return number + 1

def add(number1, number2):
    total_sum = number1

    for i in range(number2):
        total_sum = plus_one(total_sum)
    
    return total_sum

def multiply(number1, number2):
    if number1 >= number2:
        total_product = number1
        limit = number2
        start = number1
    else:
        total_product = number2
        limit = number1
        start = number2
    
    for i in range(limit - 1):
        total_product = add(total_product, start)
    
    return total_product