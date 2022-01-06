from CoffeeMachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()

    coffee_machine.balance()
    print()
    print("Write action (buy, fill, take):")
    action = input()
    if action == 'buy':
        coffee_machine.buy()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
    print()
    coffee_machine.balance()


if __name__ == '__main__':
    main()
