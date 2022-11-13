""" All_Primes """
def main():
    """ All_Primes """
    num = int(input())
    count = 0
    for i in range(1, num+1):
        if  i > 1:
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                count += 1
    print(count)
main()
