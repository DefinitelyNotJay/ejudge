""" HxH """
def main():
    """ print edited info """
    info = input()
    details = {}
    for alp in info:
        if alp in details.keys():
            details[alp] = details[alp]+1
        else:
            details[alp] = 1
    details = sorted(details.items(), \
    key=lambda var: (ord(var[0]) + (999 if var[0].isupper() else 0)))
    txt = ""
    for key, value in details:
        while value > 0:
            if value > 5:
                txt += "-----|"
                value -= 5
            else:
                txt += value*"-"
                value -= value
        print(key, ":", txt)
        txt = ""
main()
