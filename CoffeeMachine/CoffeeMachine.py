class CoffeeMachine:
    water = 0
    milk = 0
    beans = 0

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
