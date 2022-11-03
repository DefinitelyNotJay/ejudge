""" Table I """
def main():
    """ print noodle's cost """
    num = int(input())
    for sequence in range(1, num+1):
        print("15 x %i = %d"%(sequence, 15*sequence))
main()
