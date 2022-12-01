"""[Recommend] Temperature"""
def main():
    """[Recommend] Temperature"""
    values = float(input())
    old = input()
    want = input()
    #change to c
    if old == "K":
        values = values-273.15
    elif old == "R":
        values = (values*5/9)-273.15
    elif old == "F":
        values = (values-32)*5/9

    if want == "F":
        ans = (values*9/5)+32
    elif want == "K":
        ans = values+273.15
    elif want == "R":
        ans = (values+273.15)*9/5
    else:
        ans = values
    print("%.2f" %ans)
main()