""" Olympic """
def main(lap):
    """ Olympic """
    details = list()
    for _ in range(lap):
        info = input()
        details.append([[info[:3]], list(map(int, info[4:].split()))])
        details[-1][1].append(sum(details[-1][1]))
    details = sorted(details, \
    key=lambda var: (-var[1][0], -var[1][1], -var[1][2], var[0][0]))
    count, prev, stat = 0, 0, 0
    for key, value in details:
        if value != prev:
            count += stat
            stat = 0
            count += 1
        elif count != 0:
            stat += 1
        print(count, key[0], " ".join(list(map(str, value))))
        prev = value
main(int(input()))
