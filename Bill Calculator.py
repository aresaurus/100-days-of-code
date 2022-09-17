print('Welcome to the tip calculator!')
try:
    bill = float(input('What was the total bill? $'))
except ValueError:
    print('Sorry, we need a number here.')
    bill = float(input('What was the total bill? '))


percentage_tip = int(input('What percentage tip would you like to give?: 10, 12 or 15? '))
if percentage_tip == 10:
    percentage_tip = 0.10
if percentage_tip == 12:
    percentage_tip = 0.12
if percentage_tip == 15:
    percentage_tip = 0.15
  

try:
    people_bill = int(input('How many people to split the bill? '))
except ValueError:
    print('We need a number here.')
    people_bill = int(input('How many people to split the bill? '))


def calculate_tip(amount, percentage, people):
    money = ((bill * percentage_tip) + bill) / people_bill
    return money

money = calculate_tip(bill, percentage_tip, people_bill)
rounded_money = round(money, 2)

print(f'Each person should pay ${rounded_money}')

