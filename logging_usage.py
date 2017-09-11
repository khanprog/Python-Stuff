import logging


logging.basicConfig(filename='logs.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# For diabling the logging and debugging

#logging.disable(logging.CRITICAL)


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial function N is {}'.format(n))

    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('the value of i {0} and value of total is {1}'.format(i, total))

    logging.debug('Return value is {}'.format(total))
    return total

print(factorial(15))

logging.debug('End of program')
