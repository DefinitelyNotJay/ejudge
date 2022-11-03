""" SumOfNumber """

def main():
    """ print sum of all numbers """
    your_fav_result = int(input())
    total = 0
    while True:
        num = int(input())
        total += num
        if num < 0 or total == your_fav_result:
            if num < 0:
                total += 1
            break
    print(total)
main()
