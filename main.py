from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()


menu = Menu()


money_machine=MoneyMachine()

off = False

while not off:
    userchoice = input(f"Which coffee do you want? {menu.get_items()}")
    if userchoice =="report":
        coffee_maker.report()
        money_machine.report()
    elif userchoice =="off":
        off =True

    elif menu.find_drink(userchoice)!= None:

        for menu_item in menu.menu:
            if menu_item.name ==userchoice:
                if coffee_maker.is_resource_sufficient(menu_item) == True:
                    if money_machine.make_payment(menu_item.cost) ==True:
                            coffee_maker.make_coffee(menu_item)
