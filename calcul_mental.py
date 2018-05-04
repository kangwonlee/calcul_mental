"""
Mental Calculation Practice

Kangwon Lee

Initally for French Elementary School Students but anyone can use.

How to use:
    Please check the following example.

$ python calcul_mental.py
Ready?
553 + 0 + 0 + 4 + 2 = ? 559
Correct
time = 6.49737 sec
Ready?n

    The script will first ask whether you are ready. 
    Entering 'No' or 'non' would stop the program
    Otherwise, would show a question.
    Enter your answer in numbers.
    The program will tell if your answer is correct or not
    and the calculation time.

Hope this helps.
"""


import pprint
import random
import time


def main():

    history = []

    # You will be able to practice indefinitley if you want
    while True:
        ready = input('Ready?')
        # if answer starts with 'n' or 'N' the program would stop
        if ready.lower().startswith('n'):
            break
        else:

            this_one = {}
            history.append(this_one)

            # generate random numbers
            base = random.randint(1, 999)
            n1 = random.randint(1, 9)
            n2 = random.randint(1, 9)
            n3 = random.randint(1, 9)
            n4 = random.randint(1, 9)

            question_string = '%d + %d + %d + %d + %d = ? ' % (base, n1, n2, n3, n4)

            this_one['question'] = question_string

            # to measure calculation time
            start_time_sec = time.time()

            # show question and obtain answer
            answer_str = input(question_string)

            # to measure calculation time
            this_one['lap time'] = lap_time_sec = time.time() - start_time_sec
            this_one['answer'] = answer_str

            # to measure calculation time more exactly
            answer = int(answer_str)

            # compare the calculations
            if (base + n1 + n2 + n3 + n4) == answer:
                print('Correct')
                this_one['result'] = 'correct'
            else:
                print('Expected = %d' % (base + n1 + n2 + n3 + n4))
                this_one['result'] = 'could do better'

            # show calculation time
            print('time = %g sec' % (lap_time_sec))

    print('Thanks for trying.\n'
          'You will do even better next time.')
    if history:
        pprint.pprint(history)


if '__main__' == __name__:
    main()
