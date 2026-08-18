import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.info('Start of debugging')

def is_leap_year(year):
    logging.debug('YEAR SET: ' + str(year))
    if year % 4 == 0:
        logging.debug('IS YEAR A MULTIPLE OF 4? ' + str(year % 4 == 0))

        if year % 100 == 0:
            logging.debug('IS YEAR A MULTIPLE OF 100? ' + str(year % 100 == 0))

            if year % 400 == 0:
                logging.debug('IS YEAR A MULTIPLE OF 400? ' + str(year % 400 == 0))
                return True
            else:
                logging.debug('IS YEAR A MULTIPLE OF 400? ' + str(year % 400 == 0))
                return False

        logging.debug('IS YEAR A MULTIPLE OF 100? ' + str(year % 100 == 0))
        return True

    logging.debug('IS YEAR A MULTIPLE OF 4? ' + str(year % 4 == 0))
    return False

while True:
    print('Enter a year or "done":')
    response = input()
    logging.info('YEAR SET: ' + str(response))
    if response == 'done':
        break
    print('Is leap year:', is_leap_year(int(response)))