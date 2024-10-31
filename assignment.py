
redo = True
while ( redo ):
    pizza = input( "Large or Extra Large?" )
    print ("You selected", pizza)
    if pizza != "Large" and pizza != "Extra Large":
    print("We do not have that size")
    else:
    redo = False
if pizza == "Large":
    print("That costs $6")
    large = 6
    print("How many toppings, 1, 2, 3 or 4?")
    toppings = input()

    if toppings == "1":
        top_cost = 1
    elif toppings == "2":
        top_cost = 1.75
    elif toppings == "3":
        top_cost = 2.50
    elif toppings == "4":
        top_cost = 3.35
        subtotal = float(large + top_cost)
        import math
        subtotal = math.floor(subtotal * 100) / 100
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(0.13 * subtotal)
        tax = math.floor(tax * 100) / 100
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        fintot = math.floor(fintot * 100) / 100
        print("Your final cost is")
        print("$", fintot)

    
if pizza == "Extra Large":
    print("That costs $10")
    extralarge = 10
    print("How many toppings. 1, 2, 3or 4?")
    toppings = input()
    if toppings == "1":
        top_cost = 1
    elif toppings == "2":
        top_cost = 1.75
    elif toppings == "3":
        top_cost = 2.50
    elif toppings == "4":
        top_cost = 3.35
    subtotal = float(extralarge + top_cost)
    import math
    subtotal = math.floor(subtotal * 100) / 100
    print("Your subtotal is")
    print("$", subtotal)
    tax = float(0.13 * subtotal)
    tax = math.floor(tax * 100) / 100
    print("Your tax is")
    print("$", tax)
    fintot = float(tax + subtotal)
    fintot = math.floor(fintot * 100) / 100
    print("Your final cost is")
    print("$", fintot)
    