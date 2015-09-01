import sys

def ps2p1(balance, annualInterestRate, monthlyPaymentRate):
    MONTHS = 12

    def printMonthlyStatement(month, payment, balance):
        print 'Month {0}'.format(month)
        print 'Minimum monthly payment: {0:.2f}'.format(payment)
        print 'Remaining balance: {0:.2f}'.format(balance)

    def printAnnualStatement(payment, balance):
        print 'Total paid: {0:.2f}'.format(payment)
        print 'Remaining balance: {0:.2f}'.format(balance)


    remainingBalance = balance
    totalPaid = 0
    for month in range(1, MONTHS+1):
        minimumMonthlyPayment = remainingBalance * monthlyPaymentRate
        unpaidBalance = remainingBalance - minimumMonthlyPayment
        remainingBalance = unpaidBalance * (annualInterestRate / 12.0) + unpaidBalance
        printMonthlyStatement(month, minimumMonthlyPayment, remainingBalance)
        totalPaid += minimumMonthlyPayment

    printAnnualStatement(totalPaid, remainingBalance)
    return (totalPaid, remainingBalance)

def computeAnnual(balance, annualInterestRate, monthlyPayment):
    MONTHS = 12

    remainingBalance = balance
    for month in range(1, MONTHS+1):
        unpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = unpaidBalance * (annualInterestRate / 12.0) + unpaidBalance

    return remainingBalance

def ps2p2(balance, annualInterestRate):
    lowestPayment = int(balance / 120 + .5) * 10

    while computeAnnual(balance, annualInterestRate, lowestPayment) > 0:
        lowestPayment += 10

    if lowestPayment % 10 > 0:
        lowestPayment += 10 - lowestPayment % 10

    return lowestPayment

def ps2p3(balance, annualInterestRate):
    lowerBound = balance / 12
    upperBound = balance * (1+annualInterestRate/12.0)**12 / 12.0
    epsilon = 0.005

    guess = (lowerBound + upperBound) / 2
    remainingBalance = computeAnnual(balance, annualInterestRate, guess)

    while abs(remainingBalance) > epsilon:
        if remainingBalance > 0:
            lowerBound = guess
        else:
            upperBound = guess
        guess = (lowerBound + upperBound) / 2
        remainingBalance = computeAnnual(balance, annualInterestRate, guess)
    return guess

def main():
    balance = 120
    annualInterestRate = 0
    lowestPayment = ps2p3(balance, annualInterestRate)
    print 'Lowest Payment: {0:.2f}'.format(lowestPayment)


if __name__ == "__main__":
    sys.exit(int(main() or 0))