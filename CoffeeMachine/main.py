from CoffeeMachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()

    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        action = input()
        if action == 'buy':
            coffee_machine.buy()
        elif action == 'fill':
            coffee_machine.fill()
        elif action == 'take':
            coffee_machine.take()
        elif action == 'remaining':
            coffee_machine.balance()
        elif action == 'exit':
            break
        print()


if __name__ == '__main__':
    main()
