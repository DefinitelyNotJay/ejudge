""" SequenceX """

def main():
    """ print whatever this thing called """
    num = int(input())
    space1 = num * 3 - 3
    space2 = 3
    for i in range(1, num+1):
        print(" "*space1, end="")
        space1 -= 3
        for first in range(1, i+1):
            print("%02d"%first, end=" ")
        for second in range(i-1, 0, -1):
            print("%02d"%second, end=" ")
        print()
    for i in range(1, num):
        print(" "*space2, end="")
        space2 += 3
        for third in range(1, num-i+1):
            print("%02d" %third, end=' ')
        for forth in range(num-1-i, 0, -1):
            print("%02d"%forth, end=" ")
        print()
main()
