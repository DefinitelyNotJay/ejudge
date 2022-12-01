""" Scout """
def main():
    """ Go down Soft sound """
    for _ in range(int(input())):
        details = input().split()
        eggs = input().split()
        eggs = list(map(float, eggs))
        _, most, most_weight = list(map(float, details))
        eggs.sort()
        eggs = eggs[:int(most)]
        if sum(eggs) >= most_weight:
            count, total = 0, 0
            for i in eggs:
                if total + i < most_weight:
                    count += 1
                    total += i
            total = count
        else:
            total = len(eggs)
        print(total)
main()
