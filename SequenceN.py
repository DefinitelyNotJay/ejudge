""" Sequence N """

def main():
    """ print flexible N pattern """
    num = int(input())
    for row in range(1, num+1):
        for column in range(1, num+1):
            if row == column or column == 1 or column == num:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
