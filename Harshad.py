""" Harshad """
def main():
    """ print it's harshad or not """
    for _ in range(10):
        num = abs(int(input()))
        divider = 0
        for digit in str(num):
            divider += int(digit)
        if num == 0 or num % divider != 0:
            print("No")
        else:
            print("Yes")
main()
