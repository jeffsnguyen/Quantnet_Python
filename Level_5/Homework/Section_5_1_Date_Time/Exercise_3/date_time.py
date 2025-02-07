# Type: Homework
# Level: 5
# Section: 5.1 Date/Time
# Exercise: 3
# Description: Contains the tests for various Date/Time operations
#   Modify the above program to request the user enter the date in the following format (for example):
#       2016 September 25 06:24:14:12342 PM
#######################
# Importing necessary packages
import logging
import datetime
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')


###############################################
def main():
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    # Testing block
    # Scenario:
    #   This block will:
    #       ab. Handle datetime input in the format: 2016 September 25 06:24:14:12342 PM
    #       cde. Handle extraction of parameters: year, month, day, hour, minute, second, microseconds.
    #           d. Print out in 2016-09-25 18:23:14:12342
    #           e. Print out in 2016 September 25 06:24:14:12342 PM
    #       f. Do d e with current local time
    #       g. Do d e with current UTC time

    #######################
    # Test ab
    testNum = 'Test ab'
    logging.info(f'{testNum}')
    print('ab. Handle datetime input in the format: 2016 September 25 06:24:14:12342 PM')
    logging.info('ab. Handle datetime input in the format: 2016 September 25 06:24:14:12342 PM')
    # 2020-09-23 1:6:30:123456
    # Taking user inputs
    logging.info('Taking user inputs')
    date_time = input('Enter date time 2016 September 25 06:24:14:12342 PM = ')

    if 'AM' in date_time:  # Check string input for 'AM'
        try:  # Exception Handling block to handle datetime conversion
            # 1. Take string input
            # 2. Split 'AM' from the input
            # 3. Grab the index 0 item and strip it
            # 4. Convert to a datetime variable and immediately convert it back to string with AM/PM format
            date_time = datetime.datetime.strptime(date_time.split('AM')[0].strip(), '%Y %B %d %I:%M:%S:%f')
            date_timeSTR = date_time.strftime('%Y %B %d %I:%M:%S:%f %p')
        except Exception as Ex:
            print(f'Failed. Incorrect format. See log for more details.')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            print(f'{date_timeSTR}')
            logging.info(f'Input accepted. {date_timeSTR}')
            pass
    elif 'PM' in date_time:
        try:  # Exception Handling block to handle datetime conversion
            date_time = datetime.datetime.strptime(date_time.split('PM')[0].strip(), '%Y %B %d %I:%M:%S:%f')
        except Exception as Ex:
            print(f'Failed. Incorrect format. See log for more details.')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            # Add 12 hours because PM and strftime it back to AM/PM string format
            date_time = date_time + datetime.timedelta(hours=12)
            date_timeSTR = date_time.strftime('%Y %B %d %I:%M:%S:%f %p')
            print(f'{date_timeSTR}')
            logging.info(f'Input accepted. {date_timeSTR}')
            pass
    else:
        print('Invalid format.')
        logging.error('Invalid format.')

    print()

    # Parameters extractions
    logging.debug('Start parameter extraction.')

    year = date_time.year
    month = date_time.month
    day = date_time.day
    hour = date_time.hour
    minute = date_time.minute
    second = date_time.second
    microsecond = date_time.microsecond
    # Display the extracted parameters:
    logging.info('Displaying the parameters.')
    print(f'Year: {year}\n'
          f'Month: {month}\n'
          f'Day: {day}\n'
          f'Hour: {hour}\n'
          f'Minute: {minute}\n'
          f'Second: {second}\n'
          f'Microsecond: {microsecond}\n')
    print()

    logging.info(f'#######################{testNum} Completed.')
    #######################


###############################################


#######################
if __name__ == '__main__':
    main()
