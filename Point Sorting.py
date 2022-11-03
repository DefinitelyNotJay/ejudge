""" Point Sorting """
def distance(val):
    """ checked function """
    return val[0] + val[1], -val[1]
def main(amount):
    """ print sorting point """
    for _ in range(amount):
        case = []
        for _ in range(int(input())):
            info = input().split()
            case.append((int(info[0]), int(info[1])))
        case.sort(key=distance)
        for num in case:
            print(num[0], num[1])
main(int(input()))
