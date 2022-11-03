""" test loop """

def main():
    """ just loop """
    num = int(input())
    space = num*3 - 3
    for i in range(1, num+1):
        count = 0
        # print(" "*space, end="")
        # space -= 3
        for k in range(num-i+1, 0, -1):
            print(num-count, end=" ")
            count += 1
        print()
main()
