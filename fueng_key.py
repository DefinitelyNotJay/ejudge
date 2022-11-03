""" key """
def main():
    """ key """
    num_id = input()
    countter = 0
    for carr in num_id:
        countter += int(carr)
    seconds = num_id[-3:]
    seconds = int(seconds)*10
    finall = countter+seconds
    if len(str(finall)) > 3:
        print(str(finall)[-4:])
    else:
        print(finall+1000)
main()
