""" LargestNumber """

def main():
    """ print result """
    num1 = input()
    num2 = input()
    num3 = input()
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num1 < num2:
        num1, num2 = num2, num1
    print(int(str(num1)+str(num2)+str(num3)))
main()
