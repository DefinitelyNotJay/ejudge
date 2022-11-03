""" Kaprekar """
def mod_num(num):
    """ sorting number """
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    num4 = int(num[3])
    if num1 < num2:
        num2, num1 = num1, num2
    if num2 < num3:
        num3, num2 = num2, num3
    if num3 < num4:
        num3, num4 = num4, num3
    if num1 < num2:
        num2, num1 = num1, num2
    if num2 < num3:
        num3, num2 = num2, num3
    if num1 < num2:
        num2, num1 = num1, num2
    result = str(num1)+str(num2)+str(num3)+str(num4)
    return int(result), int(result[::-1])
def main(num):
    """ 6174 """
    count = 0
    while num != 6174:
        most, least = mod_num(str(num))
        num = most-least
        length = len(str(num))
        if length != 4:
            num = "0"*(4-length) + str(num)[-length:]
        count += 1
    print(count)
main(input())
