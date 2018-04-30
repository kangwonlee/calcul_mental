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


import random
import time


def main():

    # You will be able to practice indefinitley if you want
    while True:
        ready = input('Ready?')
        # if answer starts with 'n' or 'N' the program would stop
        if ready.lower().startswith('n'):
            break
        else:
            # generate random numbers
            base = random.randint(0, 999)
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            n3 = random.randint(0,9)
            n4 = random.randint(0,9)

            question_string = '%d + %d + %d + %d + %d = ? ' % (base, n1, n2, n3, n4)
            start_time_sec = time.time()
            answer = int(input(question_string))
            lap_time_sec = time.time() - start_time_sec

            if (base + n1 + n2 + n3 + n4) == answer:
                print('Correct')
            else:
                print('answer = %d' % (base + n1 + n2 + n3 + n4))

            print('time = %g sec' % (lap_time_sec))


if '__main__' == __name__:
    main()
