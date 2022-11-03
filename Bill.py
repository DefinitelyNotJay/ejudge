"""Bill"""
def main():
    """print total expense"""
    num = int(input())
    ser = (num*10)/100
    total_ser = 0
    if ser >= 50 and ser < 1000:
        total_ser += ser
    else:
        if ser < 50:
            total_ser += 50
        else:
            total_ser += 1000
    vat = (total_ser+num) * (7/100)
    print("%.2f"%(num+total_ser+vat))
main()
