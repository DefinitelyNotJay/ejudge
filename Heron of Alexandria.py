""" Heron of Alexandria """
def main(val1, val2, val3):
    """ print HERON """
    total = (val1 + val2 + val3)/2
    area = (total*(total-val1)*(total-val2)*(total-val3))**0.5
    print("%.3f"%area)
main(float(input()), float(input()), float(input()))
