# Problem #2, "Paying Debt Off in a Year"
initial_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = interest_rate / 12
minimum_payment = 0
balance = initial_balance
months_needed = 0

while balance > 0:
    minimum_payment += 10
    balance = initial_balance
    months_needed = 0

    while months_needed < 12 and balance > 0:
        months_needed += 1
        interest = monthly_interest_rate * balance
        balance -= minimum_payment
        balance += interest

balance = round(balance, 2)

print "RESULT"
print "Monthly payment to pay off debt in 1 year: ", minimum_payment
print "Number of months needed: ", months_needed
print "Balance: ", balance

