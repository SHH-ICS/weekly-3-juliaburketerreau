print("Large or Extra Large?")
pizza = input()
if pizza == "Large":
    print("That costs $6")
    large = 6
    print("How many toppings, 1, 2, 3 or 4?")
    toppings = input()
    if toppings == "0":
        subtotal = float(large)
        import math
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(large * 0.13)
        tax = math.floor(tax * 100) / 100
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        fintot = math.floor(fintot * 100) / 100
        print("Your final cost is")
        print("$", fintot)
    if toppings == "1":
        subtotal = float(large + 1.00)
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
    if toppings == "2":
        subtotal = float(large + 1.75)
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
    if toppings == "3":
        subtotal = float(large + 2.50)
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
    if toppings == "4":
        subtotal = float(large + 3.35)
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
    print("How many toppings?")
    toppings = input()
    if toppings == "0":
        subtotal = float(extralarge)
        import math
        print("Your subtotal is")
        print("$", subtotal)
        tax = float(extralarge * 0.13)
        tax = math.floor(tax * 100) / 100
        print("Your tax is")
        print("$", tax)
        fintot = float(tax + subtotal)
        fintot = math.floor(fintot * 100) / 100
        print("Your final cost is")
        print("$", fintot)

    if toppings == "1":
        subtotal = float(extralarge + 1.00)
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
    if toppings == "2":
        subtotal = float(extralarge + 1.75)
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
    if toppings == "3":
        subtotal = float(extralarge + 2.50)
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
    if toppings == "4":
        subtotal = float(extralarge + 3.35)
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
