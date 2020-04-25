pizza_toppings = ["cheese", "pepperoni", "artichokes", "bell peppers"]
print("We have the folowing toppings:")
for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping}\t\t(free)")
    elif topping == "artichokes":
        print(f"{topping}\t(+$0.50)")
    else:
        print(f"{topping}\t(+$0.25)")
    

