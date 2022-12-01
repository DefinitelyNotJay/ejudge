""" CoinChangev1 """
def main(price):
    """ https://www.youtube.com/watch?v=WNf30EKBDdY """
    remain, coin, divider = price, 0, 0
    while remain > 0:
        if remain < 5:
            divider = 1
        elif remain < 10:
            divider = 5
        elif remain < 25:
            divider = 10
        else:
            divider = 25
        temp = remain // divider
        coin += temp
        remain = remain - divider * temp
    print(coin)
main(int(input()))
