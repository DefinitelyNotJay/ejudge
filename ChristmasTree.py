""" ChristmasTree """
def main():
    """ print flexible """
    leaves = int(input())
    wood = int(input())
    space = leaves - 1
    count = 1
    for i in range(1, leaves+1):
        print(" "*space, end="")
        space -= 1
        for _ in range(1, i+1):
            print("*", end="")
        if i > 1:
            print("*"*count, end="")
            count += 1
        print()
    for _ in range(1, wood+1):
        print(" "*(leaves-2), end="")
        print("---")
main()
