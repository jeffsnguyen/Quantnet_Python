# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains Loan class methods, modified to handle exception
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
from asset.asset import Asset
import logging

#######################
#######################

# loan class
# This class object takes on the arguments asset, face, rate, term
class Loan(object):

    # Initialization function with asset, face, rate, term
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, notional, rate, term, asset):

        # Main attributes
        self._notional = notional
        self._rate = rate
        self._term = term

        if not isinstance(asset, Asset):
            logging.error('Something wrong with parameters type.')   # Log the error prior to raising it
            raise ValueError('asset must be of Asset type.')
        else:
            self._asset = asset

    # Wrapper to display
    def __repr__(self):
        return f'Loan({self._notional}, {self._rate}, {self._term}, {self._asset})'

    ##########################################################

    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set notional value
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the attribute rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set interest rate
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute term
    @property
    def term(self):
        return self._term

    # Decorator to set loan term
    @term.setter
    def term(self, iterm):
        self._term = iterm  # Set instance variable term from input

    # Decorator to create a property function to define the attribute asset

    @property
    def asset(self):
        return self._asset

    # Decorator to set loan asset value
    @asset.setter
    def asset(self, iasset):
        self._asset = iasset  # Set instance variable asset from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    # Instance method to calculate monthly payments
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, period=None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate monthlyPayment')
            return self.calcMonthlyPmt(self._notional, self.getRate(period), self._term)
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate total payments
    def totalPayments(self):
        # Calculate total payment using the formula total = monthlyPayment * term * 12
        # r = monthly rate, P = notional value, N = term in months
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate totalPayments using monthlyPayments and term')
            return self.monthlyPayment() * self._term * 12
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate total interest over the entire loan
    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment = notional value
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate totalInterest using totalPayments and notional')
            return self.totalPayments() - self._notional
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate interest due at time t
    # This method use the given formula
    def interestDue(self, t):
        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate totalInterest using totalPayments and notional')
        return Loan.monthlyRate(self.getRate(t)) * self.balance(t - 1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate principalDue using monthlyPayments and interestDue')
        return Loan.monthlyPayment(t) - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    # Modified to delegate to calcBalance(face, rate, term, period)
    # Notional is equivalent to face
    def balance(self, t):
        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate balance using calcBalance')
        return self.calcBalance(self._notional, self.getRate(t), self._term, t)

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warn('Step: You are running a recursive function. This will take a long time.')

        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, return notional * monthlyRate if term = 1')
            return self._notional * Loan.monthlyRate(self.getRate(t))
        else:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, '
                          'return balanceRecursive(t-1) * monthlyRate if term != 1')
            return self.balanceRecursive(t - 1) * Loan.monthlyRate(self.getRate())

    # Instance method to calculate principal due at time t
    # This method use the recursive function
    def principalDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warn('Step: You are running a recursive function. This will take a long time.')

        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate principalDueRecursive, return monthlyPayment - interestDueRecursive')
        return self.monthlyPayment() - self.interestDueRecursive(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the recursive function
    def balanceRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warn('Step: You are running a recursive function. This will take a long time.')

        if t > self._term:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate balanceRecursive, '
                          'return notional - princiaplDueRecursive if term = 1')
            return self._notional - self.principalDueRecursive(t)
        else:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, '
                          'return balanceRecursive(t-1) - principalDueRecursive if term != 1')
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)

    # Instance method to get interest rate from Loan object.
    def getRate(self, period=None):
        # Capture step/job done to debug
        logging.debug('Step: Trying to get rate by simply returning rate parameters.')
        return self._rate

    # Instance method to return the current asset value for the given period times a recovery multiplier of .6
    def recoveryValue(self, t):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate recoveryValue by asset.value(t) * .6.')

        if t > self._term:
            logging.info('t value is greater than term')

        return self._asset.value(t) * .6

    # Instance method to return the available equity (current asset value less current loan balance)
    def equity(self, t):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate equity by asset.value(t) - balance(t).')

        if t > self._term:
            logging.info('t value is greater than term')

        return self._asset.value(t) - self.balance(t)
    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    # Class method to calculate the monthly payment of the given loan
    # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate calcMonthlyPmt')
            return (Loan.monthlyRate(rate) * face * (1 + Loan.monthlyRate(rate)) ** (term * 12)) / \
                   (((1 + Loan.monthlyRate(rate)) ** (term * 12)) - 1)
        except ZeroDivisionError:
            logging.error('Something went wrong. Division by 0.')  # Log the error prior to raising it
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate calcBalance')
        return face * ((1 + Loan.monthlyRate(rate)) ** period) - \
               (Loan.calcMonthlyPmt(face, rate, term) * (((1 + Loan.monthlyRate(rate)) ** period - 1) /
                                                         Loan.monthlyRate(rate)))

    ##########################################################
    # Add static method functionalities to loan class

    # Static method to return monthly rate for a passed in annual rate
    # Monthly rate = Annual Rate / 12
    @staticmethod
    def monthlyRate(annual_rate):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate monthlyRate')
        return annual_rate / 12

    # Static method to return annual rate for a passed in monthly rate
    # Annual rate = Monthly Rate * 12
    @staticmethod
    def annualRate(monthly_rate):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate annualRate')
        return monthly_rate * 12
    ##########################################################
