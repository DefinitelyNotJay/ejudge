"""Donut"""
def main():
    """Donut"""
    price = float(input())
    donut = float(input())
    free = float(input())
    need = float(input())
    times_buy = need//donut
    have_nofree = times_buy*donut
    have_nofree = times_buy*donut
    if need == 1:
        times_buy = 1
    elif have_nofree >= need:
        times_buy = times_buy-1
    have_nofree = times_buy*donut
    have_justfree = times_buy*free
    you_have = have_nofree+have_justfree
    pay = have_nofree*price
    if you_have >= need:
        print(int(pay), int(you_have))
main()
