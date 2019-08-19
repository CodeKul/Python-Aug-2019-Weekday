import random

while True:
    no1 = int(input('Enter a number between 1-10: '))
    if no1 == 0:
        print('Bye bye!')
        break
    no2 = random.randint(1, 10)

    if no1 == no2:
        print('Winner winner chicken dinner!')
    else:
        print('Better luck next time!')