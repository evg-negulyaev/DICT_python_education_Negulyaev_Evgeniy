from CoffeeMachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()

    print("Write how many ml of water the coffee machine has:")
    coffee_machine.water = int(input())
    print("Write how many ml of milk the coffee machine:")
    coffee_machine.milk = int(input())
    print("Write how many grams of coffee beans the coffee machine:")
    coffee_machine.beans = int(input())

    print("Write how many cups of coffee you will need:")
    num_of_cups = int(input())
    coffee_machine.available(num_of_cups)


if __name__ == '__main__':
    main()
