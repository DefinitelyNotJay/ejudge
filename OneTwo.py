""" OneTwo """
def cal(num):
    """ 1212312121 """
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        return cal(num-1) + cal(num-2)
def main():
    """ ฝนรักแอ๋วทองคูณ """
    total = str()
    total += cal(int(input()))
    print(total)
main()
