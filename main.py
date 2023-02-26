from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mymenu = Menu()
mymoneymachine = MoneyMachine()
mycoffeemaker = CoffeeMaker()


off=False

drinks_list = mymenu.get_items()

while off==False:
    choice = input(f"What would you like? ({drinks_list}): ")
    if choice == 'report':
        mycoffeemaker.report()
        mymoneymachine.report()
    elif choice == 'off':
        off = True
    else:
        drink = mymenu.find_drink(choice)
        enoughresources = mycoffeemaker.is_resource_sufficient(drink)
        if enoughresources == True:
            cost=drink.cost
            mymoneymachine.make_payment(cost)
            mycoffeemaker.make_coffee(drink)


