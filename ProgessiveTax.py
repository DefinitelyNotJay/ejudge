""" ProgressiveTax """
def main():
    """ print tax you'll need to pay """
    cash = float(input())
    paid, percent = 0, 0
    if 0 < cash <= 150000:
        print(0)
    elif cash < 300001:
        paid, percent = cash-150000, 5
    elif cash < 500001:
        paid, percent = cash-300000, 10
    elif cash < 750001:
        paid, percent = cash-500000, 15
    elif cash < 1000000:
        paid, percent = cash-750000, 20
    elif cash < 2000001:
        paid, percent = cash-1000000, 25
    elif cash < 4000001:
        paid, percent = cash-2000000, 30
    else:
        paid, percent = cash-150000, 35
    cash -= 

        
