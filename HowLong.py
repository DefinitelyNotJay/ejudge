""" HowLong """

def main():
    """ print len(num) in different way """
    num = abs(float(input()))
    accumulator = 0
    divider = 1
    while True:
        if num // divider > 0:
            accumulator += 1
        elif num == 0:
            accumulator += 1
            break
        else:
            break
        divider *= 10
    print(accumulator)
main()
