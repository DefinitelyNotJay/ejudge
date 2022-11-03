""" Parity """
def main(num, option):
    """ parity checking """
    count = 0
    for each_num in num:
        if each_num == "1":
            count += 1
    if (option == 'Even' and count % 2 == 0) or (option == 'Odd' and count % 2 != 0):
        num += '0'
    else:
        num += '1'
    print(num)
main(input(), input())
