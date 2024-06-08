#this code contains modules from different classes.
#go to: https://replit.com/@devmoh04/oop-coffee-machine-final#coffee_maker.py for coffee maker receipe
#go to: https://replit.com/@devmoh04/oop-coffee-machine- final#menu.py for menu card
#go to: https://replit.com/@devmoh04/oop-coffee-machine-final#money_machine.py for money related calculations

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("Welcome to the COFFEE MACHINE!!")
menu.print_item_costs()

while is_on:
    options = menu.get_items()
    
    choice = input(f"What would you like to have from {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
