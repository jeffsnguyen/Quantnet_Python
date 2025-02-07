# Type: Homework
# Level: 3
# Section: 3.3: Exception Handling
# Exercise: 3
# Description: Contains the tests for handling multiple exception via calculating a factorial
#   Create a function that calculates the factorial of an input number. If the input value is invalid, raise
#       an exception. Test this out in main(), and handle the exception. Provide several examples, using
#       explicit error handling and general error handling (catching all error types).

#######################
# Importing necessary packages

#######################

###############################################
# Return the factorial of num
def factorial(num):
    if not num >= 0:  # Check if the integer is positive
        raise ValueError('Must be a positive number')
    else:
        result = 1
        for n in range(2, num+1):
            result *= n
        return result
###############################################
def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test 1. Handling both specific and general exception
    #       2. Test 2. Handling both only general exception
    ###############################################

    # Test 1. Handling both specific and general exceptions
    print('Test 1. Handling both specific and general exceptions.')
    # Program takes 1 input from user, handle input exception

    try:  # catching string input exception
        x = int(input('Input a number: '))  # take input
    except ValueError:  # handle non-number exception, for example: string
        print(ValueError('Must be an integer'))
        pass
    else:
        try:  # catching other exception related to factorial, e.g. can't be negative
            print(str(x) + '! = ' + str(factorial(x)))
        except ValueError as valEx:
            print(valEx)
            pass
        except Exception:  # handle other unknown exception
            print(Exception('Unknown error: '))
    pass
    print()

    # Test 2. Handling both only general exceptions
    print('Test 2. Handling only general exceptions.')
    # Program takes 1 input from user, handle strictly general exceptions
    try:  # catching string input exception
        x = int(input('Input a number: '))  # take input
    except Exception as Ex:  # handle non-number exception, for example: string
        print(Ex)
        pass
    else:
        try:  # catching other exception related to factorial, e.g. can't be negative
            print(str(x) + '! = ' + str(factorial(x)))
        except Exception as Ex:  # handle other unknown exception
            print(Ex)
    pass
    print()


###############################################

#######################
if __name__ == '__main__':
    main()