""" Sequence IX """

def main():
    """ Sequence IX """
    num = int(input())
    space = num*3-3
    for row in range(1, num+1):
        print(" "*space, end="")
        space -= 3
        for k in range(1, row+1):
            print("%02d"%k, end=" ")
        if row >= 2:
            for reverse in range(row-1, 0, -1):
                print("%02d"%reverse, end=" ")
        print()
main()
