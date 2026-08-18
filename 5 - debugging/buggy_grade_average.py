import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of debugging')

def calculate_grade_average(grade_sum, number_of_grades):
    logging.debug('grade_sum is ' + str(grade_sum) + ' and number of grades is ' + str(number_of_grades))
    try:
        grade_average = int(grade_sum / number_of_grades)
    except ZeroDivisionError:
        return 0

    logging.info('The calculate_grade_average return value is ' + (str(grade_average)))
    return grade_average

counter = 0
total = 0

while True:
    print('Enter a grade, or "done" if done entering grades:')
    grade = input()
    logging.info('The input set is ' + str(grade))
    if grade == 'done':
        break
    counter = counter + 1
    logging.debug('The grades counted until now are ' + str(counter))
    total = total + int(grade)
    logging.debug('The total amount of the grades is actually ' + str(total))

logging.info('COUNTER: ' + str(counter) + ' | TOTAL: ' + str(total))
avg = calculate_grade_average(total, counter)
print('The grade average is:', avg)