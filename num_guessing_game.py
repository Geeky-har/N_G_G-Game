import random

main = random.randint(1, 100)

print('Enter any number between 1 to 100')

no_of_att = 10

count = 0

while no_of_att >= 0:
    count = count + 1
    no_of_att = no_of_att - 1
    user = int(input())
    if user > main:
        print('Decrease your number')
        print(f'No. of attempts left {no_of_att} ')

    elif user < main:
        print('Increase your number')
        print(f'No of attempts left {no_of_att} ')

    else:
        print('You Won')
        print(f'Congratulations You won in {count}th attempt')

