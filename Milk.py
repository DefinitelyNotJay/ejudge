""" MILK """
def main(a_value, b_value, c_value, d_value):
    """ print most milk possible """
    cap = d_value // a_value
    milk = cap
    if b_value == 0:
        print(milk)
    else:
        while True:
            more = (cap // b_value) * c_value
            milk += more
            mod = (cap % b_value)
            cap = 0
            cap += mod
            cap += more
            more = 0
            if cap < b_value:
                break
        print(milk)
main(int(input()), int(input()), int(input()), int(input()))
