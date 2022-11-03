"""Calculator"""
def main():
    """Calculator"""
    num = int(input())
    nub = 0
    if num == 1:
        print(1)
    else:
        for i in range(1, num+1):
            nub += int(len(str(i)))+1
        print(nub)
main()
