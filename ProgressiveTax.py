""" ProgressiveTax """
def classified(income):
    """ longlongcode :| """
    income /= 100000
    if income <= 3:
        cut_off, percent = 1.5, 5
    elif income <= 5:
        cut_off, percent = 3, 10
    elif income <= 7.5:
        cut_off, percent = 5, 15
    elif income <= 10:
        cut_off, percent = 7.5, 20
    elif income <= 20:
        cut_off, percent = 10, 25
    elif income <= 40:
        cut_off, percent = 20, 30
    else:
        cut_off, percent = 40, 35
    return cut_off*100000, percent/100

def main():
    """ TaxTax """
    income = float(input())
    cut_off = 0
    percent = 1
    if income <= 150000:
        print(0)
    else:
        cut_off, percent = classified(income)
        lost = (income - cut_off) * percent
        # print(income, cut_off, percent)
        print(int(lost))
main()
