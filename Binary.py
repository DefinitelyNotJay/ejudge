""" Binary """
def cal(num, total):
    """ print binary """
    if num == 0:
        print(0)
        return
    if num < 0 or num == 1:
        total += str(num%2)
        total += str(num//2)
        print(int(total[::-1]))
        return
    else:
        total += str(num%2)
        num = num//2
        cal(num, total)
cal(int(input()), "")
