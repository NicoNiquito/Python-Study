# Tip Calculator

print('Welcome to the Tip Calculator')

total_bill = input('What was the total bill? ')
percentage = input('What percentage tip would you like to give? 10, 12 or 15? ')
split = input('How many people to split the bill? ')

percentage2 = int(percentage) / 100

total_mult_perc = float(total_bill) * percentage2
total_plus_percentage = float(total_bill) + total_mult_perc

divided_bill = round(total_plus_percentage, 2) / int(split)

print(round(divided_bill, 2))
