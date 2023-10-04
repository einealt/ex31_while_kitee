# Are you going to Kitee?
# while and if

print("Lähdetkö Kiteelle?")
print("1. Lähden")
print("2. En lähde")
choice1 = input("> ")

while choice1 == "1":
    print("Jos miettisit vielä?")
    print("1. Mietin vielä")
    print("2. En mieti")
    choice2 = input("> ")
        
    if choice2 == "1":
        print("Lähdetkö Kiteelle?")
        print("1. Lähden")
        print("2. En lähde")
        choice3 = input("> ")
        
        if choice3 == "2":
            exit(".")

    if choice2 == "2":
        destination = ["Berliiniin", "Kööpenhaminaan", "Tampereelle"]
        count = len(destination)
        print(f"Mutta tässä olisi {count} vaihtoehtoista matkakohdetta:")
        for dest in destination:
            print(f"Voisit lähteä {dest}.")
        print("Lähdetkö silti Kiteelle?")

if choice1 == "2":
        exit(".")
else:
        print("Just näin.")

