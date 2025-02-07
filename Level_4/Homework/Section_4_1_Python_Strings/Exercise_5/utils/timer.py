# Type: Homework
# Level: 4
# Section: 4.1: Python Strings
# Exercise: 5
# Description: This contains the class Timer
#   Convert your Timer class’ print statement to use f-Strings instead of concatenating strings.

# Importing packages
from time import time


# Timer class
# This class object takes on hours, minutes, seconds arguments
# It also has functionalities to count time elapsed and configure format of said time elapsed
class Timer(object):

    # Initialization function with hours, minutes and seconds arguments
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, timerName):
        self._timerName = timerName

    # Start the context (timer)
    def __enter__(self):
        self.start = time()  # Call start() to start timer
        print('Starting timer, wait for process to complete...')
        return self

    # Exit the context (timer)
    def __exit__(self, *args):  # Call end() to get timer result and end the timer
        self.end = time()
        print('End timer.')
        print(f'{self.timerName}: {self.end-self.start} {self.timer_dict[self.timer_config]}.')

    # Initialize a counter instance variable to check if timer has/ has not started
    # Initial value is False: timer not started
    timer_check = False

    # Initialize objects to format elapsed time in seconds, minutes or hours
    # Initialize timer_config variable to format the displayed elapsed time, default is 1
    timer_config = 1
    # Initialize dictionary to lookup proper string to display 'seconds', 'minutes' or 'hours'
    timer_dict = {1: 'seconds', 60: 'minutes', 3600: 'hours'}

    ##########################################################
    # Decorators to define and set values for instance variables

    # Decorator to create a property function to define the argument seconds
    @property
    def timerName(self):
        return self._timerName

    # Decorator to set seconds
    @timerName.setter
    def timerName(self, itimerName):
        self._timerName = itimerName  # Set instance variable seconds from input

    ##########################################################
    # Class method functions to perform some actions

    # Default time function to set default time
    @classmethod
    # Set at the class level the value of hours, minutes, seconds as default if not speicified
    # Instead of storing dhours, dminutes and dseconds at the object level, store them at the class level
    def defaultTime(cls, timerName):
        # Get values of each class variable from the instance object
        cls._timerName = timerName

    ##########################################################
    # Instance methods

    # Instance method to start time counter
    def start(self):
        if self.timer_check:
            print('Error: Timer already running. Please wait...')
        else:
            print('Starting timer, wait for process to complete...')
            self.counter_start = time()
            self.timer_check = True

    # Instance method to end time counter
    # This also check if the timer is running. If not, print an error message
    # If the timer is running, print the time taken and return this value to the function
    def end(self):
        if not self.timer_check:  # If timer is not running, print error message
            print('Error: Timer is not running. Use start to start timer.')
        else:  # If timer is not running:
            self.counter_end = time()  # Take the time stamp of the timer with time()
            print('End timer.')  # Inform user that timer has ended.

            # Calculate time elapsed in given configuration
            self.time_elapsed_default = self.counter_end - self.counter_start
            self.time_elapsed = (self.counter_end - self.counter_start) / self.timer_config

            # Display result in correct timer configuration format
            # try except to handle exception of time configuration not existing in timer_dict dictionary
            # Only valid keys: 1: seconds, 60: minutes, 3600: hours
            try:
                print(f'Function took {self.time_elapsed} {self.timer_dict[self.timer_config]} to run.')
            except KeyError as keyEx:
                print(f'Time config {keyEx} is not valid. Result will be displayed in seconds (config = 1).')
                print(f'Function took {self.time_elapsed_default} seconds to run.')

            self.timer_check = False  # Reset the check variable

    # Instance method to retrieve last timer result
    # Last timer configuration is used
    def retrieveLastResult(self):
        self.last_result = self.time_elapsed
        # try except to handle exception of time configuration not existing in timer_dict dictionary
        # Only valid keys: 1: seconds, 60: minutes, 3600: hours
        try:
            print(f'The last timer is: {self.last_result} {self.timer_dict[self.timer_config]}.')
        except KeyError as keyEx:
            print(f'Time config {keyEx} is not valid. Result will be displayed in seconds (config = 1).')
            print(f'Function took {self.time_elapsed_default} seconds to run.')
        return self.last_result

    # Instance method to accept time display configuration
    def timerConfig(self, itimer_config):
        # Set time config based on user input
        # sec = 1 = seconds
        # min = 60 = minutes
        # hrs = 3600 = hours
        if itimer_config == 'sec':
            self.timer_config = 1
        elif itimer_config == 'min':
            self.timer_config = 60
        elif itimer_config == 'hrs':
            self.timer_config = 3600
        else:  # if input lookup fail, raise value error to user
            raise ValueError('Timer config invalid.')
        print(f'Time is currently configured to display in {self.timer_dict[self.timer_config]}.')
