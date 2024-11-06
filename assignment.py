
redo = True
while ( redo ):
    pizza = input( "Large or Extra Large? " )
    print ("You selected", pizza)
    if pizza != "Large" and pizza != "Extra Large":
        print("We do not have that size")
    else:
        redo = False
if pizza == "Large":
    print("That costs $6")
    large = 6
    redo = True
    while redo == True:
        toppings = input("How many toppings, 1, 2, 3 or 4? ")
        if toppings == "1":
            top_cost = 1
            redo = False
        elif toppings == "2":
            top_cost = 1.75
            redo = False
        elif toppings == "3":
            top_cost = 2.50
            redo = False
        elif toppings == "4":
            top_cost = 3.35
            redo = False
        else:
            print("we do not have that")
            print("We only have 1, 2, 3 or 4 toppings")
            
    
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
    redo = True
    while redo == True:
        toppings = input("How many toppings. 1, 2, 3 or 4? ")
        if toppings == "1":
            top_cost = 1
            redo = False
        elif toppings == "2":
            top_cost = 1.75
            redo = False
        elif toppings == "3":
            top_cost = 2.50
            redo = False
        elif toppings == "4":
            top_cost = 3.35
            redo = False
        else:
            print("we do not have that")
            print("We only have 1, 2, 3 or 4 toppings")
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
    