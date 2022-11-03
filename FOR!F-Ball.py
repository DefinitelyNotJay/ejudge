""" FOR!F-Ball """
def find_a_ball(swap, cur_ball):
    """ finding where the ball really is """
    if swap == 'A' and (cur_ball == 1 or cur_ball == 3):
        if cur_ball == 1:
            return 2
        else:
            return 1
    if swap == 'B' and (cur_ball == 2 or cur_ball == 3):
        if cur_ball == 2:
            return 3
        else:
            return 2
    if swap == 'C' and (cur_ball == 1 or cur_ball == 3):
        if cur_ball == 1:
            return 3
        else:
            return 1
    else:
        return cur_ball

def main():
    """ call function """
    text = input().upper()
    current_ball = 1
    for swap in text:
        current_ball = find_a_ball(swap, current_ball)
    print(current_ball)
main()
