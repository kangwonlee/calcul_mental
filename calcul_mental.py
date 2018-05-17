"""
Mental Calculation Practice

Kangwon Lee

Initally for French Elementary School Students but anyone can use.

How to use:

    The script will first ask whether you are ready. 
    Entering 'No' or 'non' would stop the program
    Otherwise, would show a question.
    Enter your answer in numbers.
    The program will tell if your answer is correct or not
    and the calculation time.

    Please check the following example:

$ python calcul_mental.py
Ready?
115 + 9 + 5 + 5 + 7 = ? 141
Correct
time = 26.2807 sec
Ready?
262 + 5 + 4 + 8 + 1 = ? 180
'180' does not seem to be a valid answer.
Please try again :)
262 + 5 + 4 + 8 + 1 = ? 280
Correct
time = 15.6669 sec
Ready?n
Thanks for trying.
You will do even better next time.
[{'answer': '141',
  'lap time': 26.280706882476807,
  'question': '115 + 9 + 5 + 5 + 7 = ? ',
  'result': 'correct'},
 {'answer': '280',
  'lap time': 15.666854858398438,
  'question': '262 + 5 + 4 + 8 + 1 = ? ',
  'result': 'correct'}]

Hope this helps.
"""


import pprint
import random
import time


def main():

    # to keep records
    history = []

    # You will be able to practice indefinitley if you want
    while True:
        ready = input('Ready?')
        # if answer starts with 'n' or 'N' the program would stop
        if ready.lower().startswith('n'):
            break
        else:

            # to record this attempt
            this_one = {}
            # to preserve this record in the history
            # this may happen at the end the else block
            history.append(this_one)

            # generate random numbers
            base = random.randint(1, 999)
            n1 = random.randint(1, 9)
            n2 = random.randint(1, 9)
            n3 = random.randint(1, 9)
            n4 = random.randint(1, 9)

            question_string = '%d + %d + %d + %d + %d = ? ' % (base, n1, n2, n3, n4)

            # record question
            this_one['question'] = question_string

            # to measure calculation time
            start_time_sec = time.time()

            # to give students more opportunities
            answer = False

            while not answer:

                # show question and obtain answer
                answer_str = input(question_string)

                # to measure and record calculation time
                this_one['lap time'] = lap_time_sec = time.time() - start_time_sec
                # record answer ; int() may fail
                this_one['answer'] = answer_str

                try:
                    # to measure calculation time more exactly, convert to int here
                    answer = int(answer_str)
                except ValueError:
                    answer = False

                # to retry if not correct, evaluate in the while loop
                # compare the calculations
                if (base + n1 + n2 + n3 + n4) == answer:
                    print('Correct')
                    # record result
                    this_one['result'] = 'correct'
                else:
                    # to retry if not correct
                    answer = False
                    # record result, believing the student could give correct answer later
                    this_one['result'] = 'could do better'
                    # Retry message for unexpected answers
                    print('%r does not seem to be a valid answer.\n'
                          'Please try again :)' % (answer_str))

            # show calculation time
            print('time = %g sec' % (lap_time_sec))

    print('Thanks for trying.\n'
          'You will do even better next time.')
    if history:
        # present history if not empty
        # because it can be long, using pprint.pprint() for now
        pprint.pprint(history)


if '__main__' == __name__:
    main()
