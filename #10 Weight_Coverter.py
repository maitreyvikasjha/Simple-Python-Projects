weight = int(input("Weight : "))
unit = input("L(Lbs) OR K(kg) ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f" You are {converted} Kilos")
else:
    converted = weight / 0.45
    print(f" You are {converted} Pounds")
