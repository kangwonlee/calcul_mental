import pprint
import random
import time


def main():
    # to keep records
    history = []

    # for variable challange level
    config = {
        'n_numbers': 2,
        'min_number': 2,
        'max_number': 12,
        'operations': [
            {
                'name': 'mul', 
                'answer': lambda xy: xy[0] * xy[1], 
                'question_str': lambda xy:f"{xy[0]} * {xy[1]}",
            },
            {
                'name': 'div', 
                'answer': lambda xy: xy[0], 
                'question_str': lambda xy:f"{xy[0]*xy[1]} / {xy[1]}",
            },
        ],
    }

    # keep track of student's achievement
    doing_great = 0

    while is_ready():
        this_one = {}

        history.append(this_one)

        question_dict = get_question(config)

        this_one['question'] = question_dict['question_string']

        start_time_sec = time.time()

        answer = False

        while not answer:

            answer_str = input(question_dict['question_string'] + ' = ? ')

            this_one['lap time'] = lap_time_sec = time.time() - start_time_sec
            this_one['answer'] = answer_str

            try:
                # to measure calculation time more exactly, convert to int here
                answer = int(answer_str)
            except ValueError:
                answer = False

            if is_correct(question_dict, answer):
                doing_great = did_great(this_one, doing_great)
            else:
                answer, doing_great = will_do_better(this_one, answer_str, doing_great)
        print('time = %g sec' % (lap_time_sec))

    finish(history)

    return history


def get_question(config):

    min_number = config['min_number']
    max_number = config['max_number']
    n_numbers = config['n_numbers']

    operand_list = [random.randint(min_number, max_number) for i in range(n_numbers)]

    operation = random.choice(config['operations'])

    question_string = operation['question_str'](operand_list)

    return {
        'operand_list': operand_list,
        'operation': operation,
        'question_string': question_string,
    }


def is_correct(question_dict, answer):
    return question_dict['operation']['answer'](question_dict['operand_list']) == answer


def did_great(this_one, doing_great, smily_face='^3^'):
    print(f'Correct {smily_face}')
    this_one['result'] = 'correct'

    return doing_great + 1


def will_do_better(this_one, answer_str, doing_great):
    answer = False

    this_one['result'] = 'could do better'
    print(f'{repr(answer_str)} does not seem to be a valid answer.\n'
        'Please try again :)')

    return answer, doing_great + (-1)


def finish(history):
    print('Thanks for trying.\n'
            'You will do even better next time.')
    if history:
        # present history if not empty
        # because it can be long, using pprint.pprint() for now
        pprint.pprint(history)


def is_ready():
    result = False

    while True:

        ready = input('Ready? ').strip().strip('.').lower()

        if ready.startswith('n'):
            result = False
            break
        elif ready.startswith('y'):
            result = True
            break
        elif not ready:
            result = True
            break
        else:
            print('yes or no please?')

    return result


if "__main__" == __name__:
    main()
