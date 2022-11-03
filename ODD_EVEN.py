""" ODD_EVEN """

def is_odd():
    """ print True or False """
    num = int(input())
    if num % 2 == 0:
        print(False)
    else:
        print(True)

def main():
    """ call is_odd function """
    is_odd()
main()
