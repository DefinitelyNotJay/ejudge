""" ฟิโบนาชชี่รีเคอชั่นชั่นชั่น """
def cal(num):
    """ ฟังก์ชั่นคิดคำนวณ """
    if num <= 1:
        return num
    else:
        return cal(num-1) + cal(num-2)
def main():
    """ รีเคอชั่น """
    print(cal(int(input())))
main()
