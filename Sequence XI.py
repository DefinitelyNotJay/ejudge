""" Sequence XI """

from turtle import numinput


def main():
    """ print cube """
    num_input = int(input())
    num = 2 * num_input - 1
    starter_num = 1
    for row in range(1, num+1):
        for column in range(1, num+1):
            if row == column and row == num_input and column == num_input:
                print("%02d"%num_input, end=" ")
            else:
                print("%02d"%0, end=" ")
            # print(column, end=" ")
        print()
main()
