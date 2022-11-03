""" Grade II """
def cal_grade(num):
    """ grade finding """
    if num < 0 or num > 100:
        print("ERR")
    elif num < 60:
        print("F")
    elif num < 65:
        print("F+")
    elif num < 70:
        print("D")
    elif num < 75:
        print("D+")
    elif num < 80:
        print("C")
    elif num < 85:
        print("C+")
    elif num < 90:
        print("B")
    elif num < 95:
        print("B+")
    elif num <= 100:
        print("A")
def main():
    """ call function cal_grade """
    score = float(input())
    cal_grade(score)
main()
