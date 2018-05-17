"""
Mental Calculation Practice

Kangwon Lee

Initally for French Elementary School Students but anyone can try.

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

    # for variable challange level
    n_addend = 4
    min_addend = 1
    max_addend = 9

    # keep track of student's achievement
    doing_great = 0

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

            # generate augend
            question_list = [random.randint(1, 999)]

            # revise challenge level
            n_addend, min_addend, max_addend, doing_great = revise_challenge(n_addend, min_addend, max_addend, doing_great)

            # generate addends
            question_list += generate_addends(n_addend, min_addend, max_addend)

            # to generate the question using str.join()
            question_string_list = [str(q) for q in question_list]

            # generate the question
            question_string = ' + '.join(question_string_list)

            # record question
            this_one['question'] = question_string

            # to measure calculation time
            start_time_sec = time.time()

            # to give students more opportunities
            answer = False

            while not answer:

                # show question and obtain answer
                answer_str = input(question_string + ' = ? ')

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
                if sum(question_list) == answer:
                    print('Correct')
                    # record result
                    this_one['result'] = 'correct'

                    # This student is doing great
                    doing_great += 1
                else:
                    # to retry if not correct
                    answer = False
                    # record result, believing the student could give correct answer later
                    this_one['result'] = 'could do better'
                    # Retry message for unexpected answers
                    print('%r does not seem to be a valid answer.\n'
                          'Please try again :)' % (answer_str))

                    # This student will be doing great
                    doing_great += -1

            # show calculation time
            print('time = %g sec' % (lap_time_sec))

    print('Thanks for trying.\n'
          'You will do even better next time.')
    if history:
        # present history if not empty
        # because it can be long, using pprint.pprint() for now
        pprint.pprint(history)
    
    return history


def generate_addends(n_addend, minimum=1, maximum=9):
    """
    n_addend : number of addends
    minimum : minimum of an addend. 1 by default
    maximum : maximum of an addend. 9 by default
    """

    # generate addends
    addends_list = []

    for _ in range(n_addend):
        addends_list.append(random.randint(1, 9))

    return addends_list


def revise_challenge(n_addend, min_addend, max_addend, doing_great):

    # if a student is doing great, make the problem slightly more challenging
    if 5 < doing_great:
        min_addend = get_min(doing_great)

        # if a student seems doing consistently good, increase the number of addends
        if 4 < min_addend:
            n_addend += 1
            # reset other challenge level parameters
            doing_great, max_addend, min_addend = reset_all_level_params(doing_great, min_addend, max_addend)

    # if a student is not doing great, make the problem slightly more comfortable
    elif -4 > doing_great :
        if 6 < max_addend :
            max_addend = 6
            doing_great = reset_doing_great(doing_great)
        else:
            max_addend += (-1)
            doing_great = reset_doing_great(doing_great)

        if 5 > max_addend:
            n_addend = max((1, n_addend - 1))
            # reset other challenge level parameters
            doing_great, max_addend, min_addend = reset_all_level_params(doing_great, min_addend, max_addend)

    return n_addend, min_addend, max_addend, doing_great


def get_min(doing_great):
    return (doing_great // 3) + 1


def reset_all_level_params(doing_great, min_addend, max_addend):
    doing_great = reset_doing_great(doing_great)
    min_addend = 1
    max_addend = 9
    return doing_great, max_addend, min_addend


def reset_doing_great(doing_great):
    doing_great = int(doing_great * 0.8)
    return doing_great


if '__main__' == __name__:
    main()
