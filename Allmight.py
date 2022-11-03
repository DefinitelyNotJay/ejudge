""" One For All """
def main():
    """ ------ """
    result = ""
    num = int(input())
    for seq in range(1, num+1):
        name = input()
        if seq == num:
            result += name + "_" + str(seq)
        elif seq % 2 != 0:
            result += name + ("*"*seq)
        elif seq % 2 == 0:
            result += name + ("-"*seq)
    print(result)
main()
