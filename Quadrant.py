""" Quadrant """

def main():
    """ find q """
    var_x = int(input())
    var_y = int(input())
    if var_x > 0 and var_y > 0:
        print('Q1')
    elif var_x > 0 and var_y < 0:
        print('Q4')
    elif var_x < 0 and var_y < 0:
        print('Q3')
    elif var_x < 0 and var_y > 0:
        print('Q2')
    elif var_x == 0 and var_y == 0:
        print("O")
    elif var_y == 0:
        print("X")
    elif var_x == 0:
        print("Y")
main()
