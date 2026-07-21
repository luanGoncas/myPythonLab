def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while True:
    try:
        print('Enter number:')
        number = int(input())

        current_value = number
        print(number, end=' ')

        while current_value != 1:
            print(collatz(current_value), end=' ')
            current_value = collatz(current_value)
        break
    except ValueError:
        print('You must enter an integer number')