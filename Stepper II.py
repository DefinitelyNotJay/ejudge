""" Stepper II """

def main():
    """ print result """
    num1 = int(input())
    num2 = int(input())
    remain = abs(num1 - num2)
    if num1 > num2:
        for i in range(remain+1):
            print(num1-i)
    else:
        for k in range(remain+1):
            print(num1+k)
main()
