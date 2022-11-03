""" Hamburger """

def main():
    """ print our beloved hamburger """
    left_bread = int(input())
    right_bread = int(input())
    pork = (left_bread + right_bread) * 2
    print("|"*left_bread + "*"*pork + "|"*right_bread)
main()
