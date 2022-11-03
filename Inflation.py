""" Inflation """
def main():
    """ print product price after k years"""
    num = float(input())
    year = int(input())
    for _ in range(year):
        num = num + num*3.81/100
        # ตัดเศษที่เกิน 2
        dot_po = str(num).find(".")
        num = float(str(num)[:dot_po+3])
    print("%.2f"%(num))
main()
