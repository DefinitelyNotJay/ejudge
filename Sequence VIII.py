""" Sequence VIII """

def main():
    """ ----- """
    num = int(input())
    space_count = num * 3 - 3
    for i in range(1, num+1):
        print(" "*space_count, end="")
        space_count -= 3
        for number in range(1, i+1):
            print("%02d"%number, end=" ")
        print()
main()
