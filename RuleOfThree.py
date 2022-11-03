""" RuleofThree """
def main():
    """ print worthy snack (weight per gram)"""
    col = []
    lap = int(input())
    result, price, weight = 0, 0, 0
    for _ in range(lap):
        each_price = float(input())
        each_weight = float(input())
        tiny_list = [each_price, each_weight, each_weight/each_price]
        col.extend([tiny_list])
    for num in range(len(col)):
        cur_price = col[num][0]
        cur_weight = col[num][1]
        cur_avg = col[num][2]
        if cur_avg > result:
            result = cur_avg
            price, weight = cur_price, cur_weight
        if cur_avg == result:
            result = cur_avg
            if price > cur_price:
                price, weight = cur_price, cur_weight
    print("%.2f %.2f"%(price, weight))
main()
