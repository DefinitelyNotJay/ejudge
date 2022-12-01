""" Temperature """
def default(tempt, option, change):
    """ WEDNESDAY """
    if option == 'R':
        tempt = (tempt*5/9)-273.15
    elif option == 'F':
        tempt = (tempt-32)*5/9
    elif option == 'K':
        tempt = tempt-273.15
    if change == 'F':
        ans = (tempt*9/5)+32
    elif change == 'K':
        ans = tempt+273.15
    elif change == 'R':
        ans = (tempt+273.15)*9/5
    else:
        ans = tempt
    print("%.2f"%ans)
default(float(input()), input(), input())
