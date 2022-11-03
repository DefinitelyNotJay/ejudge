""" GraderMachine """

def main():
    """ ควย """
    first_num = int(input())
    last_num = int(input())
    eiei = 0
    print("pass : ", end="")
    if first_num > last_num:
        for i in range(first_num, last_num-1, -1):
            if i%2 == 0:
                eiei += i
                print(i, end=" ")
        print()
        print("Sum :", eiei)
    else:
        for i in range(first_num, last_num+1):
            if i%2 == 0:
                eiei += i
                print(i, end=" ")
        print()
        print("Sum :", eiei)
main()
