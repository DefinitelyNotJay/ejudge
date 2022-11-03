""" Classify """
def main():
    """ print edited info """
    info = input()
    details = {}
    while info != "END":
        if info[:4] in details.keys():
            details[info[:4]] = details[info[:4]]+1
        else:
            details[info[:4]] = 1
        info = input()
    details = sorted(details.items(), \
    key=lambda var: (int(var[0][:2]), int(var[0][2:4])))
    prev = details[0][:2]
    result = ""
    for key, value in details:
        if key[:2] != prev:
            result = key[:2]
        else:
            result = "--"
        print(result, int(key[2:4]), value)
        prev = key[:2]
main()
