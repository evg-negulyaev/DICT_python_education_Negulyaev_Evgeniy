from CoffeeMachine import CoffeeMachine


def main():
    coffee_machine = CoffeeMachine()

    while coffee_machine.state != 'EXIT':
        command = ''
        if coffee_machine.state == 'CHOICE_OF_ACTION':
            print("Write action (buy, fill, take, remaining, exit): ")
            command = input()
        elif coffee_machine.state == 'CHOICE_OF_COFFEE':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ', end='')
            command = input()
        elif coffee_machine.state == 'REFILLING':
            print("Write how many ml of water you want to add: ", sep='')
            water = input()
            print("Write how many ml of milk you want to add: ", sep='')
            milk = input()
            print("Write how many grams of coffee beans you want to add: ", sep='')
            beans = input()
            print("Write how many disposable coffee cups you want to add: ", sep='')
            cups = input()
            command = water + ' ' + milk + ' ' + beans + ' ' + cups
        coffee_machine.method(command)
        print()


if __name__ == '__main__':
    main()
