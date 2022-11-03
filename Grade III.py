""" Grade III """

def cal_grade(num):
    """ grade finding """
    score = 0
    if num < 60:
        score += 0
    elif num < 65:
        score += 0.5
    elif num < 70:
        score += 1
    elif num < 75:
        score += 1.5
    elif num < 80:
        score += 2
    elif num < 85:
        score += 2.5
    elif num < 90:
        score += 3
    elif num < 95:
        score += 3.5
    elif num <= 100:
        score += 4
    return score
def main():
    """ call function cal_grade """
    num = int(input())
    total = 0
    for _ in range(num):
        total += cal_grade(float(input()))
    grade = str(total/num)
    result = ""
    count = 0
    for cha in grade:
        if count > 3:
            break
        result += cha
        count += 1
    if len(result) == 3:
        result += "0"
    print(result)
main()
