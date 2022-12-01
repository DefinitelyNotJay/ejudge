""" Dart """
def main():
    """ It's not living if it's not with you """
    score = 0
    for _ in range(int(input())):
        info = input().split()
        var_x, var_y = int(info[0]), int(info[-1])
        var_x = var_y if var_y > var_x else var_x
        if var_x < 2:
            score += 5
        elif var_x < 4:
            score += 4
        elif var_x < 6:
            score += 3
        elif var_x < 8:
            score += 2
        elif var_x < 10:
            score += 1
        print(var_x, "score", score)
    print(score)
main()
