class CoffeeMachine:
    coffee_dict: dict = {
        "water": 0,
        "milk": 0,
        "coffee_beans": 0,
        "disposable_cups": 0,
        "money": 0
    }

    espresso: dict = {
        "water": 250,
        "milk": 0,
        "coffee_beans": 16,
        "disposable_cups": 1,
        "money": 4,
        "title": "espresso"
    }

    latte: dict = {
        "water": 350,
        "milk": 75,
        "coffee_beans": 20,
        "disposable_cups": 1,
        "money": 7,
        "title": "latte"
    }

    cappuccino: dict = {
        "water": 200,
        "milk": 100,
        "coffee_beans": 12,
        "disposable_cups": 1,
        "money": 6,
        "title": "cappuccino"
    }

    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.coffee_dict["water"] = water
        self.coffee_dict["milk"] = milk
        self.coffee_dict["coffee_beans"] = coffee_beans
        self.coffee_dict["disposable_cups"] = disposable_cups
        self.coffee_dict["money"] = money

    def fill_machine(self, water, milk, coffee_beans, disposable_cups):
        self.coffee_dict["water"] += water
        self.coffee_dict["milk"] += milk
        self.coffee_dict["coffee_beans"] += coffee_beans
        self.coffee_dict["disposable_cups"] += disposable_cups

    def take_money(self):
        self.coffee_dict["money"] = 0

    @staticmethod
    def exit_program():
        exit(0)

    def remaining(self):
        self.print_state()

    def print_state(self):
        print("The coffee machine has:\n",
              self.coffee_dict["water"], "of water\n",
              self.coffee_dict["milk"], "of milk\n",
              self.coffee_dict["coffee_beans"], "of coffee beans\n",
              self.coffee_dict["disposable_cups"], "of disposable cups\n",
              self.coffee_dict["money"], "of money\n")

    def can_prepare(self, coffee_type):
        is_enough = min(
            self.coffee_dict["water"] - coffee_type["water"],
            self.coffee_dict["milk"] - coffee_type["milk"],
            self.coffee_dict["coffee_beans"] - coffee_type["coffee_beans"],
            self.coffee_dict["disposable_cups"] - coffee_type["disposable_cups"]
        )
        return is_enough > 0

    def buy_coffee(self, coffee_type):
        if self.can_prepare(coffee_type):
            self.coffee_dict["water"] -= coffee_type["water"]
            self.coffee_dict["milk"] -= coffee_type["milk"]
            self.coffee_dict["coffee_beans"] -= coffee_type["coffee_beans"]
            self.coffee_dict["disposable_cups"] -= coffee_type["disposable_cups"]
            self.coffee_dict["money"] += coffee_type["money"]
            print("I have enough resources, making you a coffee!")
        else:
            print("Not enough components for", coffee_type["title"])

    def fill(self):
        water = int(input("Write how many ml of water you want to add:\n"))
        milk = int(input("Write how many ml of milk you want to add:\n"))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        disposable_cups = int(input("Write how many disposable coffee cups you want to add:\n"))
        self.fill_machine(water, milk, coffee_beans, disposable_cups)

    def take(self):
        print("I gave you", self.coffee_dict["money"])
        self.take_money()

    def select_coffee(self):
        coffee_list = {
            "1": self.espresso,
            "2": self.latte,
            "3": self.cappuccino
        }
        user_buy_action = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                    "menu:\n"))
        if user_buy_action == "back":
            return
        if user_buy_action in coffee_list:
            self.buy_coffee(coffee_list[user_buy_action])
        else:
            print("Wrong selection, pls repeat your choose")
            self.select_coffee()

    def action_select(self):
        action_list = {
            "buy": self.select_coffee,
            "fill": self.fill,
            "take": self.take,
            "remaining": self.remaining,
            "exit": self.exit_program
        }
        user_action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
        if user_action in action_list:
            action_list.get(user_action)()
        else:
            print("Wrong selection, pls repeat your choose")
            return


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.print_state()
    while True:
        coffee_machine.action_select()

