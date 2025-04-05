def ex01():
    age = int(input('Enter your age: '))

    if age > 18:
        print('Eligible for voting')
    else:
        print('Not eligible for voting')

def ex02():
    num = int(input('Enter a number: '))

    if num % 2 == 0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is a odd number')

def ex03():
    num = int(input('Enter a number: '))

    if num % 7 == 0:
        print(f'{num} is divisible by 7')
    else:
        print(f'{num} is not divisible by 7')

def ex04():
    num = input('Enter a number: ')

    if num[-1] % 3 == 0:
        print('True')
    else:
        print('False')

def ex06():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    num = int(input('Enter a number: '))
    if num > 1 and num < 7:
        print(days[num - 1])
def ex05():
    import random as random

    num = random.randint(1, 9)

    guess_num = int(input('Enter a number: '))

    if num == guess_num:
        print('true')
    else:
        print(f'false, the right number is {num}')

if __name__ == '__main__':
    ex05()