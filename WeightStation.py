""" WeightStation """

def cal_balance(weight, avg):
    """ return boolean value whether it's balance or not """
    if abs(avg - weight) <= avg / 2:
        return 0
    else:
        return 1

def get_balance_stat(weight1, weight2, weight3, weight4, avg):
    """ get balance status """
    count = 0
    count += cal_balance(weight1, avg)
    count += cal_balance(weight2, avg)
    count += cal_balance(weight3, avg)
    count += cal_balance(weight4, avg)
    # print(count)
    return count

def find_forth_weight(avg_weight, weight_2, weight_3, weight_4):
    """ calculate forth weight """
    weight_left = 4 * avg_weight - (weight_2 + weight_3 + weight_4)
    total_weight = weight_left + weight_2 + weight_3 + weight_4
    weight_stat = True
    balance_stat = True
    if total_weight > 15000:
        weight_stat = False
    # print("weight_stat :", weight_stat)
    overweight_counter = get_balance_stat(weight_left, weight_2, weight_3, weight_4, avg_weight)
    if overweight_counter != 0:
        balance_stat = False
    # print("balance_stat :", balance_stat)
    if weight_stat == True and balance_stat == True:
        print("Pass %.2f"%weight_left)
    else:
        if weight_stat == False and balance_stat == False:
            print("Overweight")
        elif balance_stat == False and weight_stat == True:
            print("Unbalance")
        else:
            print("Overweight")

def main():
    """ print truck status """
    find_forth_weight(float(input()), float(input()), float(input()), float(input()))
main()
    