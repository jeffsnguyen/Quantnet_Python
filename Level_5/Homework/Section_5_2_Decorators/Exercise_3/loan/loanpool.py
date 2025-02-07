# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains LoanPool class methods
#   Add logging statements to your Loan class. This should consist of the following:
#       a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the
#           initialization function), log an error prior to raising the exception.
#       b. Debug-level logs which display interim steps of calculations and return values for the Loan functions.
#       c. Info-level logs to display things like ‘t is greater than term’ in the loan functions.
#       d. At the point the exception is caught (in your main function) use logging.exception to display
#           the exception in addition to a custom message.
#       e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to
#           take a long time, so the explicit versions are recommended).


# Importing packages
from loan.loan_base import Loan
import logging

# LoanPool Class
class LoanPool(object):
    def __init__(self, loans=None):
        self._loans = loans
        self._loan = [loan for loan in self._loans]
        self._notional = [loan.notional for loan in self._loans]
        self._rate = [loan.rate for loan in self._loans]
        self._term = [loan.term for loan in self._loans]
    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute loans

    @property
    def loans(self):
        return self._loans

    # Decorator to set loans value
    @loans.setter
    def loans(self, iloans):
        self._loans = iloans  # Set instance variable loans from input

    ##########################################################
    # Add instance methods

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackNotionals(self):
        return [loan.notional for loan in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackRates(self):
        return [loan.rate for loan in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackTerms(self):
        return [loan.term for loan in self._loans]

    # Instance method
    # Get the aggregate remaining loan balance for a given period
    def totalPayments(self, t=0):
        # Capture step/job done to debug
        logging.debug('Step: Calculate totalPayments(t).')
        return sum([loan.balance(t) for loan in self._loans])

    # Instance method
    # Get the total loan principal
    def totalPrincipal(self):
        # Capture step/job done to debug
        logging.debug('Step: Calculate totalPrincipals.')
        return sum(self._notional)

    # Instance method
    # Get the aggregate payment due for a given period
    def paymentDue(self, t=0):
        # Capture step/job done to debug
        logging.debug('Step: Calculate paymentDue(t).')
        return sum([loan.monthlyPayment(t) for loan in self._loans])

    # Instance method
    # Get the aggregate interest due for a given period
    def totalInterest(self, t=0):
        # Capture step/job done to debug
        logging.debug('Step: Calculate totalInterest(t).')
        return sum([loan.interestDue(t) for loan in self._loans])

    # Instance method
    # Get the aggregate principal due for a given period
    def principalDue(self, t=0):
        # Capture step/job done to debug
        logging.debug('Step: Calculate principalDue.')
        return self.paymentDue(t) - self.totalInterest(t)

    # Instance method
    # Get the count of loan with positive balance for a given period
    def activeLoanCount(self, t):
        count = 0
        # Capture step/job done to debug
        logging.debug('Step: Calculate activeLoanCount.')
        for loan in self._loans:
            if loan.balance(t) > 0:
                count += 1
        return count

    # Instance method
    # Calculate Weighted Average Maturity of loans in the pool
    def WAM(self):
        # Capture step/job done to debug
        logging.debug('Step: Calculate sum totalPrincipal.')

        sum_amount = self.totalPrincipal()   # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAM_rate = 0  # Initialize WAR rate to be 0

        # Capture step/job done to debug
        logging.debug('Step: Calculate WAM.')

        for loan in self._loans:
            WAM_rate += loan.notional * loan.term / sum_amount
        return WAM_rate

    # Instance method
    # Calculate Weighted Average Rate of loans in the pool
    def WAR(self):
        # Capture step/job done to debug
        logging.debug('Step: Calculate sum totalPrincipal.')

        sum_amount = self.totalPrincipal()  # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAR_rate = 0  # Initialize WAR rate to be 0

        logging.debug('Step: Calculate WAM.')

        for loan in self._loans:
            WAR_rate += loan.notional * loan.rate / sum_amount
        return WAR_rate
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
