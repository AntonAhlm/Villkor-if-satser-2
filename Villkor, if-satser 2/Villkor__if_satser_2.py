
pris=float(input("Hur Mycket Kostar Bensinen?"))

if pris<= 10:
    print("Det var billigt!")

elif pris>10.00 and pris <= 15.00:
    print("Tanka full tank")

elif pris>15 and pris < 20:
    print("Tanka tio liter")

elif pris >= 20 and pris < 25:
    print("Nu saljer jag bilen och cyklar istallet")
