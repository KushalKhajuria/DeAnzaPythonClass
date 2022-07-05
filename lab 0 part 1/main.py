number = float(input("Enter a number: "))

miles = number
kilometers = miles * 1.609
print(miles, "miles is equal to about", kilometers, "kilometers.")

kilometers = number
miles = kilometers / 1.609
print(kilometers, "kilometers is equal to about", miles, "miles.")

pounds = number
kilograms = pounds / 2.205
print(pounds, "pounds is equal to about", kilograms, "kilograms.")

kilograms = number
pounds = kilograms * 2.205
print(kilograms, "kilograms is equal to about", pounds, "pounds.")

gallons = number
liters = gallons * 3.785
print(gallons, "gallons is equal to", liters, "liters.")

liters = number
gallons = liters / 3.785
print(liters, "liters is equal to", gallons, "gallons.")
