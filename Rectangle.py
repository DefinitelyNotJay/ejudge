""" Rectangle """

def circumference(height, width):
    """ koo mai kean EiEi """
    return 2*(height + width)

def area(height, width):
    """ koo mai kean EiEi """
    print(height*width)

def main():
    """ koo mai kean EiEi """
    width = int((input()))
    height = int((input()))
    area(height, width)
    senrobroop = circumference(height, width)
    print(senrobroop)
main()

