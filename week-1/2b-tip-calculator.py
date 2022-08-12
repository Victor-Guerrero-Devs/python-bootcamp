total_bill = input("What was the total bill? $ ")
tip = input("What percentage tip would you like to give? 10%, 12%, or 15%? ")
people = input("How many people are splitting the bill? ")

bill = float(total_bill)
tip_percent = (int(tip) / 100) + 1
final = (bill * tip_percent) / int(people)
print("Each person should pay: $" + str(round(final, 2)))
