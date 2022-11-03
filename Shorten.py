""" Shorten """
def main():
    """ get shorten shirt """
    result = ""
    num = int(input())
    prev_num = num
    count = 0
    while num != -1:
        if prev_num+1 != num:
            if count == 0:
                result += str(num) + ", "
            else:
                result += "-" + str(num) + ", "
            count == 0
        elif count == 0:
            result += str(num)
        else:
            count += 1
        count += 1
        prev_num = num
        num = int(input())
    print(result)
main()
