""" Restaurant """
def main():
    """ print Eve's effort """
    food = float(input())
    promo = float(input())
    sale = float(input())
    extra = float(input())
    if food >= promo:
        normal = food*(100-sale)/100
    else:
        normal = food

    if food+extra >= promo:
        extra = (food+extra)*((100-sale)/100)
    else:
        extra = food + extra

    diff = abs(extra - normal)
    if extra > normal:
        print('No %.3f'%diff)
    elif extra < normal:
        print('Yes %.3f'%diff)
    else:
        print('Yes')
main()
