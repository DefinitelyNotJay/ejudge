""" Perfect """
def gcd(num):
    """ isprime_large """
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def main(num):
    """ https://www.youtube.com/watch?v=CLUaQCHZlzI """
    total, check = 0, 0
    for i in range(2, num):
        if not gcd(i):
            perfect_num = (2 ** (i - 1)) * ((2 ** i) - 1)
            print(perfect_num)
            check = 0
    # print(total)
main(abs(int(input())))
