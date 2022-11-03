""" WeightStation """

def main():
    """ print truck stat """
    avg = float(input())
    weight_2 = float(input())
    weight_3 = float(input())
    weight_4 = float(input())
    weight_1 = 4 * avg - (weight_2 + weight_3 + weight_4)
    total_weight = weight_1 + weight_2 + weight_3 + weight_4
    half_avg_weight = avg / 2
    if total_weight > 15000:
        print("Overweight")
    elif abs(avg - weight_1) > half_avg_weight or\
        abs(avg - weight_2) > half_avg_weight or\
        abs(avg - weight_3) > half_avg_weight or\
        abs(avg - weight_4) > half_avg_weight:
        print("Unbalance")
    else:
        print("Pass %.2f"%weight_1)
main()
