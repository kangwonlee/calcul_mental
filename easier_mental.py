import fractions
import os
import pprint
import random
import re
import time


class OperationBase(object):
    min_number = 2
    max_number = 9
    except_these = (5, 10)

    def __init__(self, n_ints=2):

        self.n_ints = n_ints
        self.pick_list = self.get_pick_list()

        # TODO : consider making this a private attribute
        self.question = self.get_question()

    def __del__(self):
        del self.question
        del self.pick_list

    @classmethod
    def get_pick_list(cls):
        pick_list = list(range(cls.min_number, cls.max_number))

        for except_this in cls.except_these:
            if except_this in pick_list:
                pick_list.remove(except_this)

        return tuple(pick_list)

    def get_random_number(self):
        return random.choice(self.pick_list)

    def get_random_numbers(self):
        return random.choices(self.pick_list, k=self.n_ints)

    def get_question(self):
        return None

    def get_answer(self):
        raise NotImplementedError

    def get_question_string(self):
        raise NotImplementedError

    def ask_question(self):
        return input(self.get_question_string() + ' = ? ')

    def is_answer_correct(self, answer_str):

        try:
            result = self.eval_answer(answer_str)
        except ValueError:
            result = None

        expected = self.get_answer()

        return expected == result

    @staticmethod
    def eval_answer(answer_str):
        raise NotImplementedError


class CancelFraction(OperationBase):
    max_number = 5
    except_these = (10,)

    def get_question(self):
        xy_set = set(self.get_random_numbers())

        while 2 > len(xy_set):
            xy_set.add(self.get_random_number())

        xy_list = list(xy_set)
        xy_list.sort()

        pick = self.get_random_number()

        # TODO : consider making this more private
        question = (xy_list[0] * pick, xy_list[1] * pick)

        return question

    def get_question_string(self):

        numerator_str = str(self.question[0])
        denuminator_str = str(self.question[1])

        number_width = max((len(numerator_str), len(denuminator_str)))

        number_formatter = f" %{number_width}d "
        h_bar = '-' * len(number_formatter)

        formatter = '\n'.join((number_formatter, h_bar, number_formatter))

        return formatter % self.question[:2]

    @staticmethod
    def eval_answer(answer_str):

        num_str, den_str = answer_str.split('/')
        num = int(float(num_str))
        den = int(float(den_str))

        return num, den

    def get_answer(self):
        fr = fractions.Fraction(self.question[0], self.question[1])
        return fr.numerator, fr.denominator


class Mul(OperationBase):
    def get_question(self):
        return self.get_random_numbers()

    def get_question_string(self):
        return f"{self.question[0]} * {self.question[1]}"

    @staticmethod
    def eval_answer(answer_str):
        return int(answer_str)

    def get_answer(self):
        return self.question[0] * self.question[1]


class Div(Mul):
    def get_question_string(self):
        return f"{self.question[0] * self.question[1]} / {self.question[1]}"

    def get_answer(self):
        return self.question[0]


def main():
    # to keep records
    history = []

    operations=(Mul, Div, CancelFraction)

    # keep track of student's achievement
    doing_great = 0

    while is_ready():
        random.seed()
        this_one = {}

        history.append(this_one)

        question_obj = random.choice(operations)()

        this_one['question'] = question_obj.get_question_string()

        start_time_sec = time.time()

        answer = False

        while not answer:

            answer_str = question_obj.ask_question()

            this_one['lap time'] = lap_time_sec = time.time() - start_time_sec
            this_one['answer'] = answer_str

            if question_obj.is_answer_correct(answer_str):
                doing_great = did_great(this_one, doing_great)
                answer = True
            else:
                answer, doing_great = will_do_better(this_one, answer_str, doing_great)
        print('time = %g sec' % (lap_time_sec))

    finish(history)

    return history


def did_great(this_one, doing_great, smily_face='^3^'):
    print(f'Correct {smily_face}')
    os.system('printf \a')
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
