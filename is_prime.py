# prime numbers are greater than 1
def main():
    num = int(input())
    flag = False
    if num > 2 and num%2 != 0:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")
main()
