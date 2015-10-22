# Problem #1, "Paying the Minimum" calculator

balance = float(raw_input("Enter the outstanding balance on your credit card:"))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal:"))
min_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal:"))

monthly_interest_rate = interest_rate / 12
number_of_months = 1
total_amount_paid = 0

while number_of_months <= 12:
    min_payment = round(min_payment_rate * balance, 2)
    total_amount_paid += min_payment
    interest_paid = round(interest_rate / 12 * balance, 2)
    principle_paid = min_payment - interest_paid
    balance -= principle_paid
    print "Month: ", number_of_months
    print "Minimum monthly payment: ", min_payment
    print "Principle paid: ", principle_paid
    print "Remaining balance: ", balance
    number_of_months += 1


print "RESULT"
print "Total amount paid: ", total_amount_paid
print "Remaining balance: ", balance


















