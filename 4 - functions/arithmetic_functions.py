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

while True:
    try:
        first_number = int(input('Enter the first number: '))
        second_number = int(input('Enter the second number: '))

        if first_number < 0 or second_number < 0:
            print('Please, enter a positive number...')
            continue
        else:
            print('Add: ', add(first_number, second_number))
            print('Multiply:', multiply(first_number, second_number))
            break
    except ValueError:
        print('Please, I need you to enter a valid number...')