"""Bill"""
def main():
    """Bill"""
    money = int(input())
    service = money*0.10
    if service<50:
        service = 50
    if service>1000:
        service = 1000
    print("%.2f" %((money+service)*0.07+money+service))
main()