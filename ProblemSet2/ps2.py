import sys
MONTHS = 12

def printMonthlyStatement(month, payment, balance):
    print 'Month {0}'.format(month)
    print 'Minimum monthly payment: {0:.2f}'.format(payment)
    print 'Remaining balance: {0:.2f}'.format(balance)

def printAnnualStatement(payment, balance):
    print 'Total paid: {0:.2f}'.format(payment)
    print 'Remaining balance: {0:.2f}'.format(balance)

def computeAnnual(balance, annualInterestRate, monthlyPayment=0, monthlyPaymentRate=0.2):

    totalPaid = 0
    remainingBalance = balance
    for month in range(MONTHS):
        unpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = unpaidBalance * (annualInterestRate / 12.0) + unpaidBalance

    return remainingBalance

def ps2p1(balance, annualInterestRate, monthlyPaymentRate):
    remainingBalance = balance
    totalPaid = 0
    for month in range(MONTHS):
        minimumMonthlyPayment = remainingBalance * monthlyPaymentRate
        unpaidBalance = remainingBalance - minimumMonthlyPayment
        remainingBalance = unpaidBalance * (annualInterestRate / 12.0) + unpaidBalance
        printMonthlyStatement(month+1, minimumMonthlyPayment, remainingBalance)
        totalPaid += minimumMonthlyPayment

    printAnnualStatement(totalPaid, remainingBalance)
    return (totalPaid, remainingBalance)

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

    while True:
        guess = (lowerBound + upperBound) / 2
        remainingBalance = computeAnnual(balance, annualInterestRate, guess)
              
        if abs(remainingBalance) < epsilon:
            break
        
        if remainingBalance > 0:
            lowerBound = guess
        else:
            upperBound = guess
    print 'Lowest Payment: {0:.2f}'.format(guess)
    return guess

def main():
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))