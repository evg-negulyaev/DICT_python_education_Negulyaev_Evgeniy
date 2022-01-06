class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9

    def __init__(self):
        self.state = 'CHOICE_OF_ACTION'

    def method(self, command):
        if self.state == 'CHOICE_OF_ACTION':
            if command == 'buy':
                self.state = 'CHOICE_OF_COFFEE'
            elif command == 'fill':
                self.state = 'REFILLING'
            elif command == 'take':
                self.state = 'EXTRACTING_MONEY'
            elif command == 'remaining':
                self.state = 'REMAINING'
            elif command == 'exit':
                self.state = 'EXIT'
        elif self.state == 'CHOICE_OF_COFFEE':
            self.buy(command)
        elif self.state == 'REFILLING':
            self.fill(command)
        elif self.state == 'EXTRACTING_MONEY':
            self.take()
        elif self.state == 'REMAINING':
            self.balance()

    def make_coffee(self):
        print("Starting to make a coffee")
        print("Grinding coffee beans")
        print("Boiling water")
        print("Mixing boiled water with crushed coffee beans")
        print("Pouring coffee into the cup")
        print("Pouring some milk into the cup")
        print("Coffee is ready!")

    def calc_amount_of_ingredients(self, num_of_cups):
        print(f"For {num_of_cups} cups of coffee you will need:")
        print(f"{200 * num_of_cups} ml of water")
        print(f"{50 * num_of_cups} ml of milk")
        print(f"{15 * num_of_cups} g of coffee beans")

    def available(self, num_of_cups):
        cups_available = min((int(self.water / 200), int(self.milk / 50), int(self.beans / 15)))
        if cups_available == num_of_cups:
            print("Yes, I can make that amount of coffee")
        elif cups_available > num_of_cups:
            print(f"Yes, I can make that amount of coffee (and even {cups_available - num_of_cups} more than that)")
        else:
            print(f"No, I can make only {cups_available} cups of coffee")

    def balance(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")
        self.state = 'CHOICE_OF_ACTION'

    def buy_espresso(self):
        water = 250
        beans = 16

        if self.water < water:
            print("Sorry, not enough water!")
            return
        if self.beans < beans:
            print("Sorry, not enough beans!")
            return
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.money += 4
        self.water -= water
        self.beans -= beans
        self.disposable_cups -= 1

    def buy_latte(self):
        water = 350
        milk = 75
        beans = 20

        if self.water < water:
            print("Sorry, not enough water!")
            return
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return
        if self.beans < beans:
            print("Sorry, not enough beans!")
            return
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.money += 7
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.disposable_cups -= 1

    def buy_cappuccino(self):
        water = 200
        milk = 100
        beans = 12

        if self.water < water:
            print("Sorry, not enough water!")
            return
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return
        if self.beans < beans:
            print("Sorry, not enough beans!")
            return
        if self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.money += 6
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.disposable_cups -= 1

    def buy(self, coffee_type):
        if coffee_type == '1':
            self.buy_espresso()
            self.state = 'CHOICE_OF_ACTION'
        elif coffee_type == '2':
            self.buy_latte()
            self.state = 'CHOICE_OF_ACTION'
        elif coffee_type == '3':
            self.buy_cappuccino()
            self.state = 'CHOICE_OF_ACTION'
        elif coffee_type == 'back':
            self.state = 'CHOICE_OF_ACTION'

    def fill(self, ingredients):
        ing = ingredients.split(' ')
        # print("Write how many ml of water you want to add: ", sep='')
        self.water += int(ing[0])
        # print("Write how many ml of milk you want to add: ", sep='')
        self.milk += int(ing[1])
        # print("Write how many grams of coffee beans you want to add: ", sep='')
        self.beans += int(ing[2])
        # print("Write how many disposable coffee cups you want to add: ", sep='')
        self.disposable_cups += int(ing[3])
        self.state = 'CHOICE_OF_ACTION'

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0
        self.state = 'CHOICE_OF_ACTION'
