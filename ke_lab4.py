#ke_lab4.py
# A program that gives you the amount+interest within a set of years
# by: Kody Ellis

#Gets keybaord input for certain variables
initialAmount = float(raw_input("Enter the initial amount: "))
interestAmount = float(raw_input("Enter the interest ( as a percentage): "))
numberOfYears = int(raw_input("Enter the number of years: "))

#Makes another varibale that has the current amount of initiaAmount so when
#I change the varibake it won't affect the intialAmount.
amount = initialAmount
for years in range( numberOfYears + 1):
    print "Year:", str(years), "amount: $" + str(amount)
    amount = amount + amount * (interestAmount / 100)
