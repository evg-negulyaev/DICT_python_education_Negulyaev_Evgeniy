import argparse
from math import ceil, log, trunc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    args = parser.parse_args()

    t = args.type
    principal = args.principal
    periods = args.periods
    interest = args.interest

    if t == "diff":
        inter = interest / (12 * 100)
        s = 0
        for n in range(periods):
            month_pay = ceil(principal / periods + inter * (principal - (principal * ((n + 1) - 1)) / periods))
            print(f"Month{n+1}: payment is {month_pay}")
            s += month_pay
        overpayment = s - principal
        print(f"Overpayment = {overpayment}")
    else:
        print("invalid key")


if __name__ == '__main__':
    main()
