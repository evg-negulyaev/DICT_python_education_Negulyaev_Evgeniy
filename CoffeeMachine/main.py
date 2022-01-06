from CoffeeMachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()
    print("Write how many cups of coffee you will need:")
    num_of_cups = int(input())
    coffee_machine.calc_amount_of_ingredients(num_of_cups)


if __name__ == '__main__':
    main()
