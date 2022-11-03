""" Grade I """

def main():
    """ return Pass or Fail """
    d = {}
    for i in range(1, 10):
        num = int(input())
        d["var_%s"%(str(i))] = num
    print("-----------------------------------")
    for k in range(1, 10):
        print(d["var_%s"%str(k)])
main()
