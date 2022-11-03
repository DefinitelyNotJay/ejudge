""" Diginity """
def main():
    """ print secret password """
    while True:
        num = int(input())
        if num == 0:
            break
        remain = num
        total = 0
        while True:
            if remain < 10:
                print(remain)
                break
            else:
                for num in str(remain):
                    total += int(num)
                remain = total
                total = 0
main()
