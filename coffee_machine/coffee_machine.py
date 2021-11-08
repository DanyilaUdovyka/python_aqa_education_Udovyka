# # Stage first (variant 1)
print(".........................................STAGE FIRST...............................")

my_dictionary: dict[int, str] = {
    0: "Starting to make a coffee",
    1: "Grinding coffee beans",
    2: "Boiling water",
    3: "Mixing boiled water with crushed coffee beans",
    4: "Pouring coffee into the cup",
    5: "Pouring some milk into the cup",
    6: "Coffee is ready!",
}
for v in my_dictionary.values():
    print(v)


# Stage first (variant 2)
print(".........................................STAGE FIRST (variant 2)...............................")

text = '''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
'''
print(text)


# Stage second
print(".........................................STAGE SECOND...............................")

cup_coffee = int(input("Write how many cups of coffee you will need:"))
print("For", cup_coffee, "cups of coffee you will need:")
s_water = 200
s_milk = 50
s_coffee_beans = 15
print(s_water * cup_coffee, "ml of water")
print(s_milk * cup_coffee, "ml of milk")
print(s_coffee_beans * cup_coffee, "g of coffee beans")


# Stage third
print(".........................................STAGE THIRD...............................")

# while True:
count_water = int(input("Write how many ml of water the coffee machine has: "))
count_milk = int(input("Write how many ml of milk  the coffee machine has: "))
count_coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
count_cup_coffee = int(input("Write how many cups of coffee you will need: "))
count_available_cups = min(count_water // s_water, count_milk // s_milk, count_coffee_beans // s_coffee_beans)
# print(count_available_cups)
if count_cup_coffee > count_available_cups:
    print("No, I can make only", count_available_cups, "cups of coffee")
elif count_cup_coffee == count_available_cups:
    print("Yes, I can make that", count_available_cups, "of coffee")
elif count_cup_coffee < count_available_cups:
    print("Yes, I can make that", count_cup_coffee, "of coffee (and even", count_available_cups - count_cup_coffee,
          "more than that)")


# Stage fourth
print(".....................................STAGE FOURTH AND FIFTH.......................................")
coffee_machine_state = {
    "water": 0,
    "milk": 0,
    "coffee_beans": 0,
    "disposable_cups": 0,
    "money": 0
}


def init_state(state, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
    state["water"] = water
    state["milk"] = milk
    state["coffee_beans"] = coffee_beans
    state["disposable_cups"] = disposable_cups
    state["money"] = money


def buy_coffee(state, water, milk, coffee_beans, disposable_cups, money):
    state["water"] -= water
    state["milk"] -= milk
    state["coffee_beans"] -= coffee_beans
    state["disposable_cups"] -= disposable_cups
    state["money"] += money


def fill_machine(state, water, milk, coffee_beans, disposable_cups):
    state["water"] += water
    state["milk"] += milk
    state["coffee_beans"] += coffee_beans
    state["disposable_cups"] += disposable_cups


def take_money(state):
    state["money"] = 0


def exit_project(state):
    exit()


def remaining(state):
    print_state(coffee_machine_state)


def print_state(state):
    print("The coffee machine has:\n",
          state["water"], "of water\n",
          state["milk"], "of milk\n",
          state["coffee_beans"], "of coffee beans\n",
          state["disposable_cups"], "of disposable cups\n",
          state["money"], "of money\n")


def can_prepare(state, water, milk, coffee_beans, disposable_cups):
    is_enough = min(
        state["water"] - water,
        state["milk"] - milk,
        state["coffee_beans"] - coffee_beans,
        state["disposable_cups"] - disposable_cups
    )
    return is_enough > 0


def print_if_not_enough_components(coffee_type):
    print("Not enough components for", coffee_type)


def buy_espresso(state, espresso_water=250, espresso_milk=0, espresso_coffee_beans=16, espresso_disposable_cups=1,
                 espresso_money=4):
    if can_prepare(state, espresso_water, espresso_milk, espresso_coffee_beans, espresso_disposable_cups):
        buy_coffee(state, espresso_water, espresso_milk, espresso_coffee_beans, espresso_disposable_cups,
                   espresso_money)
        print("I have enough resources, making you a coffee!")
    else:
        print_if_not_enough_components("espresso")


def buy_latte(state, latte_water=350, latte_milk=75, latte_coffee_beans=20, latte_disposable_cups=1, latte_money=7):
    if can_prepare(state, latte_water, latte_milk, latte_coffee_beans, latte_disposable_cups):
        buy_coffee(state, latte_water, latte_milk, latte_coffee_beans, latte_disposable_cups,
                   latte_money)
        print("I have enough resources, making you a coffee!")
    else:
        print_if_not_enough_components("latte")


def buy_cappuccino(state, cappuccino_water=200, cappuccino_milk=100, cappuccino_coffee_beans=12,
                   cappuccino_disposable_cups=1, cappuccino_money=6):
    if can_prepare(state, cappuccino_water, cappuccino_milk, cappuccino_coffee_beans, cappuccino_disposable_cups):
        buy_coffee(state, cappuccino_water, cappuccino_milk, cappuccino_coffee_beans, cappuccino_disposable_cups,
                   cappuccino_money)
        print("I have enough resources, making you a coffee!")
    else:
        print_if_not_enough_components("cappuccino")


def fill(state):
    water = int(input("Write how many ml of water you want to add:\n"))
    milk = int(input("Write how many ml of milk you want to add:\n"))
    coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    disposable_cups = int(input("Write how many disposable coffee cups you want to add:\n"))
    fill_machine(state, water, milk, coffee_beans, disposable_cups)


def take(state):
    print("I gave you", state["money"])
    take_money(state)


def back(state):
    action_select(state)


def select_coffee(state):
    coffee_list = {
        "1": buy_espresso,
        "2": buy_latte,
        "3": buy_cappuccino,
        "back": back
    }
    user_buy_action = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                "menu:\n"))
    coffee_list.get(user_buy_action, lambda _: _)(state)


def action_select(state):
    action_list = {
        "buy": select_coffee,
        "fill": fill,
        "take": take,
        "remaining": remaining,
        "exit": exit_project
    }
    user_action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
    action_list.get(user_action, lambda _: _)(state)


init_state(coffee_machine_state)
print_state(coffee_machine_state)
while True:
    action_select(coffee_machine_state)

