def number_input(prompt):
    return int(input(f'{prompt}\n'))


def _get_action():
    """Gets the action input from the user."""
    return input('Write action (buy, fill, take, remaining, exit):\n')


def _exit():
    return False


class CoffeeMachine:
    """A class for virtual coffee machine objects."""
    # Dictionary describing the resource cost of each coffee
    # water, milk, beans, disposable cups, money
    coffees = {
        '1': (250, 0, 16, 1, 4),  # espresso
        '2': (350, 75, 20, 1, 7),  # latte
        '3': (200, 100, 12, 1, 6)  # cappuccino
    }

    supplies = ['water', 'milk', 'beans', 'disposable cups']

    def __init__(self):
        """Initializes a coffee machine with a set amount of supplies and money."""
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposable_cups = 9
        self.money = 550

    def main_loop(self):
        """Executes the coffee machine's functions."""
        while True:
            action = _get_action()
            method = getattr(self, '_' + action)
            if method:
                return method()
            else:
                return _exit()

    def _buy(self):
        """Asks the user what type of coffee they want."""
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if choice == 'back':
            return self.main_loop()
        if choice in CoffeeMachine.coffees.keys() and self._validate_supplies(choice)[0]:
            print('I have enough resources, making you a coffee!\n')
            self._update_supplies(choice)
            return self.main_loop()

        print(f'Sorry, not enough {self._validate_supplies(choice)[1]}!\n')
        return self.main_loop()

    def _update_supplies(self, choice):
        water_cost, milk_cost, beans_cost, cups_cost, money_cost = CoffeeMachine.coffees[choice]
        """Updates the machine's supplies and money based on the choice of drink."""
        self.water -= water_cost
        self.milk -= milk_cost
        self.beans -= beans_cost
        self.disposable_cups -= cups_cost
        self.money += money_cost
        return

    def _validate_supplies(self, choice):
        """Validates the coffee can be made, or returns the lacking ingredient."""
        supply = [self.water, self.milk, self.beans, self.disposable_cups]

        for i in range(len(supply)):
            if supply[i] >= CoffeeMachine.coffees[choice][i]:
                continue
            else:
                return False, CoffeeMachine.supplies[i]

        return True, None

    def _fill(self):
        """Adds the given amount of each item to the machine's supply."""
        self.water += number_input('Write how many ml of water you want to add:')
        self.milk += number_input('Write how many ml of milk you want to add:')
        self.beans += number_input('Write how many grams of coffee beans you want to add:')
        self.disposable_cups += number_input('Write how many disposable coffee cups you want to add:')
        print('')
        return self.main_loop()

    def _take(self):
        """Takes all money out of the coffee machine."""
        print(f'I gave you ${self.money}\n')
        self.money = 0
        return self.main_loop()

    def _remaining(self):
        """Returns a string detailing the current supply of the coffee machine."""
        first = f'{self.water} of water\n'
        second = f'{self.milk} of milk\n'
        third = f'{self.beans} of coffee beans\n'
        fourth = f'{self.disposable_cups} of disposable cups\n'
        fifth = f'{self.money} of money'
        print('\nThe coffee machine has:\n' + first + second + third + fourth + fifth + '\n')
        return self.main_loop()


coffee_machine = CoffeeMachine()
coffee_machine.main_loop()
