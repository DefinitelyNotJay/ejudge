""" Donut """

def main():
    """ print lowest budget, donut amount """
    cost = int(input())
    pieces = int(input())
    free = int(input())
    donuts_you_want = int(input())
    lap_pre = int(donuts_you_want / (pieces + free))
    all_donuts = 0
    pure_donuts = 0
    pure_donuts += pieces*lap_pre
    all_donuts += (pieces+free)*lap_pre
    if donuts_you_want - all_donuts < pieces:
        pure_donuts += donuts_you_want - all_donuts
        all_donuts += donuts_you_want - all_donuts
    else:
        pure_donuts += pieces
        all_donuts += pieces+free
    print(cost*pure_donuts, all_donuts)
main()
