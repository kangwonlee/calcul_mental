import random
import time


def main():

    while True:
        ready = input('Ready?')
        if ready.lower().startswith('n'):
            break
        else:
            # generate random numbers
            base = random.randint(0, 999)
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            n3 = random.randint(0,9)
            n4 = random.randint(0,9)

            question = '%d + %d + %d + %d + %d = ? ' % (base, n1, n2, n3, n4)
            start_time_sec = time.time()
            answer = int(input(question))
            lap_time_sec = time.time() - start_time_sec

            if (base + n1 + n2 + n3 + n4) == answer:
                print('Correct')
            else:
                print('answer = %d' % (base + n1 + n2 + n3 + n4))

            print('time = %g sec' % (lap_time_sec))


main()
