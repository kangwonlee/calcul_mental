import random
import time


def main():
    # to keep records
    history = []

    # for variable challange level
    n_numbers = 2
    min_number = 2
    max_number = 9

    # keep track of student's achievement
    doing_great = 0

    while is_ready():
        pass


def is_ready():
    result = False

    while True:

        ready = input('Ready? ').strip().lower()

        if ready.startswith('n'):
            result = False
            break
        elif ready.startswith('y'):
            result = True
            break
        else:
            print('yes or no please?')

    return result


if "__main__" == __name__:
    main()
