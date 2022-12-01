""" Inverter """
def main():
    """ INVERSE """
    num = input()
    result = str()
    for char in num:
        if char == '1':
            result += "0"
        else:
            result += "1"
    print(result.lstrip("0"))
main()
