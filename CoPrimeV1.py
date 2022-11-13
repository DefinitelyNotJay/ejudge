""" CoPrime """
def main():
    """ print CoPrime """
    num1, num2 = int(input()), int(input())
    while num2:
        num1, num2 = num2, num1%num2
    print("YES" if num1 == 1 else "NO")
    print(num1)
main()
