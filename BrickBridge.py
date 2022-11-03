""" BrickBridge """

def main():
    """ print result """
    small_b = int(input())
    large_b = int(input())
    goal_b = int(input())
    limit_b = goal_b // 5
    if large_b < limit_b:
        limit_b = large_b
    left_goal = goal_b - (limit_b*5)
    if left_goal > small_b:
        print("-1")
    else:
        print(left_goal)
main()
