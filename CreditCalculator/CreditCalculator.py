from math import ceil, log, trunc


def main():
    print('What do you want to calculate?')
    print('''type "n" for number of monthly payments, 
type "a" for annuity monthly payment amount, 
type "p" for loan principal:''')
    action = input()
    if action == 'n':
        print("Enter the loan principal:")
        payment = int(input())
        print("Enter the monthly payment:")
        month_payment = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        num = ceil(log(month_payment / (month_payment - i * payment), 1 + i))
        years = trunc(num / 12)

        months = num - years * 12
        if months == 0:
            print(f"It will take {years} years to repay this loan!")
        elif years == 0:
            print(f"It will take {months} months to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
    elif action == 'p':
        print("Enter the annuity payment:")
        a_payment = float(input())
        print("Enter the number of periods:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        loan = trunc(a_payment * ((1 + i) ** period - 1) / (i * (1 + i) ** period))
        print(f"Your loan principal = {loan}!")
    elif action == 'a':
        print("Enter the loan principal:")
        payment = int(input())
        print("Enter the number of periods:")
        period = int(input())
        print("Enter the loan interest:")
        loan_int = float(input())
        i = loan_int / (12 * 100)
        month_pay = ceil((payment * i * ((1 + i) ** period)) / (((1 + i) ** period) - 1))
        print(f"Your monthly payment = {month_pay}!")


if __name__ == '__main__':
    main()
