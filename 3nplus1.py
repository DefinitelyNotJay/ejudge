""" 3nPlus1 """
def main():
    """ How can I find another one like you """
    num = int(input())
    total = 1
    while num != 0:
        number = num
        while number > 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = number*3 + 1
            total += 1
        print(total)
        total = 1
        num = int(input())
main()
