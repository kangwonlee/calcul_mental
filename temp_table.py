def main():
    for row in range(10):
        row_list =['%2d %2d' % (row, row + col) for col in range(10)]
        row_string = ' '.join(row_list)
        print(row_string)


if '__main__' == __name__:
    main()
