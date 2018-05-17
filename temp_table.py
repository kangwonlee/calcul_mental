import calcul_mental


def main():
    for row in range(10):
        row_list =['%2d %2d' % (row, row + col) for col in range(10)]
        row_string = ' '.join(row_list)
        print(row_string)


def present_get_min():
    for doing_great in range(30):

        print('%2d %2d' % (doing_great, calcul_mental.get_min(doing_great)))


if '__main__' == __name__:
    present_get_min()
