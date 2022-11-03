""" SequenceVII """

def main():
    """ Sequence VII """
    num = int(input())
    for k in range(num):
        for rand1 in range(k+1):
            print(rand1+1, end=" ")
        print()
    for j in range(num-1, 0, -1):
        for rand2 in range(j):
            print(rand2+1, end=" ")
        print()
main()
