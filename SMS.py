""" SMS """
def main():
    """ Danny ran into some complications """
    options = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    result = list()
    for _ in range(int(input())):
        key = int(input())
        lap = int(input())
        if key == 1:
            del result[-lap:]
        elif key == 7 or key == 9:
            result.append(options[key-2][lap%4-1])
        else:
            result.append(options[key-2][lap%3-1])
    print("".join(result) if result != [] else 'null')
main()
