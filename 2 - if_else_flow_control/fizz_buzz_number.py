x = int(input())

if x % 3 == 0:
    if x % 5 == 0:
        print('Fizz Buzz')
    else:
        print('Fizz')
elif x % 5 == 0:
    print('Buzz')
else:
    print(x)