""" GraderMachine """

def main():
    """ Material qualification's clone  """
    starter = int(input())
    stopper = int(input())
    plus_value = 2
    if starter > stopper:
        if starter % 2 != 0:
            starter -= 1
        plus_value *= -1
    else:
        if starter % 2 != 0:
            starter += 1
        if stopper % 2 != 0:
            stopper -= 1
    finisher = stopper + plus_value
    text = ''
    count = 0
    for i in range(starter, finisher, plus_value):
        count += i
        text += " " + str(i)
    print("pass :" + text)
    print('Sum :', str(count))
main()
