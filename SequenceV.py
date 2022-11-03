""" Sequence V """

def main():
    """ Cap Capo Cigarettes & Beer """
    num = int(input())
    count = 7
    for i in range(num):
        if i == count:
            print("")
            count += 7
        print(num-i, end=" ")
main()
