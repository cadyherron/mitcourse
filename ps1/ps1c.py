# Problem #3, Using Bisection Search
initial_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

monthly_interest_rate = interest_rate / 12
balance = initial_balance
min_payment = balance / 12
max_payment = (balance * (1 + monthly_interest_rate) * 12.0) / 12.0
months_needed = 0

while True:
    balance = initial_balance
    monthly_payment = (min_payment + max_payment)/2

    # simulate passage of time, each iteration is 1 month
    for months_needed in range(1, 13):
        interest = round(balance * monthly_interest_rate, 2)
        balance += interest - monthly_payment
        if balance <= 0:
            break

    if max_payment - min_payment <= 0.005:
        print "RESULT"
        monthly_payment = round(monthly_payment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year: ", monthly_payment

        balance = initial_balance
        for months_needed in range(1, 13):
            interest = round(balance * monthly_interest_rate, 2)
            balance += interest - monthly_payment
            if balance <= 0:
                break
        print "Number of months needed: ", months_needed
        print "Balance: ", round(balance, 2)
        break

    elif balance < 0:
        max_payment = monthly_payment
    else:
        min_payment = monthly_payment