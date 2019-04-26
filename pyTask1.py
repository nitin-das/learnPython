weight = int(input("Weight:"))
unit = input("l(bs) for Pound or k(g) for kilos:")
if unit == 'l':
    weight_pound = weight * .45
    print(f"weight in pound is {weight_pound}")
elif unit == 'k':
    weight_kilo = weight / .45
    print(f"weight in kilos is {weight_kilo}")
else:
    print("wrong choice")