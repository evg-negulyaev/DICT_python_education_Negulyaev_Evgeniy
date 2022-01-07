from math import ceil


def main():
    print('Enter the loan principal:')
    principal = int(input())

    print('What do you want to calculate?')
    print('type "m" – for number of monthly payments, type "p" – for the monthly payment:')
    action = input()
    if action == 'm':
        print('Enter the monthly payment:')
        payment = int(input())
        print(f'It will take {ceil(principal / payment)} months to repay the loan')
    elif action == 'p':
        print('Enter the number of months:')
        periods = int(input())
        payment = ceil(principal / periods)
        last_payment = principal - (periods - 1) * payment
        if payment == last_payment:
            print(f'Your monthly payment = {payment}')
        else:
            print(f'Your monthly payment = {payment} and the last payment = {last_payment}')


if __name__ == '__main__':
    main()
