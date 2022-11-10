""" Olympic """
def main(lap):
    """ Olympic """
    details = {}
    for _ in range(lap):
        info = input()
        details[info[:3]] = list(map(int, info[4:].split()))
        details[info[:3]] += [sum(details[info[:3]])]
    details = sorted(details.items(), \
    key=lambda var: (-var[1][0], -var[1][1], -var[1][2], var[0]))
    count, prev, stat = 1, details[0][1], 0
    for key, value in details:
        print(value, prev)
        if value != prev:
            count += stat
            stat = 0
            count += 1
        elif count != 0:
            stat += 1
        print(count, key, " ".join(list(map(str, value))))
        prev = value
    # print(details)
main(int(input()))
