""" ball """
def main():
    """ print tesla's theory """
    height = float(input())
    collector = 0
    while True:
        if height < 0.01:
            break
        else:
            height *= 3/5
            collector += 1
    print(collector-1)
main()
