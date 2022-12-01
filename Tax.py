""" Tax """
def use_years(total, years):
    """ calculate discount from years """
    ans = 0
    if years < 6:
        return total
    elif years == 6:
        ans = total * 0.9
    elif years == 7:
        ans = total * 0.8
    elif years == 8:
        ans = total * 0.7
    elif years == 9:
        ans = total * 0.6
    elif years >= 10:
        ans = total * 0.5
    return ans
def main():
    """ Taxmania """
    years = int(input())
    power = int(input())
    total = 0
    if power < 600:
        total += power*0.5
    else:
        total += 600*0.5
        if power < 1800:
            total += (power-600)*1.5
        else:
            total += 1200*1.5
            total += (power-1800)*4
    print("%.2f"%use_years(total, years))
main()
