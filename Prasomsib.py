""" ---- """
def main():
    """ S[HE] BE[LIE]VE[D] """
    num = input()
    count = 0
    for i in range(len(num) - 1):
        total = 0
        for j in num[int(i):]:
            total += int(j)
            if total == 10:
                count += 1
                break
    print(count)
main()
