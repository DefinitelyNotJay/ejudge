""" Shorten """
def main():
    """ get shorten shirt """
    result = ""
    count = 1
    starter_num = int(input())
    prev_num = starter_num
    first = 0
    checker = ""
    while True:
        num = int(input())
        if num == -1:
            break
        if prev_num+1 == num:
            count += 1
            if count == 2:
                result += prev_num
                count = 0
        else:

    print(result)
main()
