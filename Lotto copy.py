""" Lotto """
def main():
    """ I still waiting my mom for winning some lottos """
    reward = []
    for _ in range(6):
        reward.append(input())
    lotto = input()
    first_prize = reward[0]
    count, total = 0, 0
    print(reward)
    for _ in range(len(reward)):
        count += 1
        # print(count, prize)
        if count == 1 and lotto == first_prize:
            total += 6000000
        elif count == 2 and lotto[-2:] == reward[1]:
            total += 2000
        elif count == 3 and (lotto[:3] == reward[2] or lotto[:3] == reward[3]):
            total += 4000
        elif count == 4 and (lotto[:3] == reward[2] or lotto[:3] == reward[3]):
            total += 4000
        elif count == 5 and (lotto[-3:] == reward[4] or lotto[-3:] == reward[5]):
            total += 4000
        elif count == 6 and (lotto[-3:] == reward[5] or lotto[-3:] == reward[4]):
            total += 4000
    side_reward1 = str(int(first_prize) - 1)
    side_reward2 = str(int(first_prize) + 1)
    # print(side_reward1, side_reward2)
    if first_prize == '999999':
        side_reward2 = '000000'
    if first_prize == '000000':
        side_reward1 = '999999'
    if len(side_reward1) != 6 or len(side_reward2) != 6:
        side_reward1 = "0"*(6-len(side_reward1)) + str(side_reward1)[-len(side_reward1):]
        side_reward2 = "0"*(6-len(side_reward2)) + str(side_reward2)[-len(side_reward2):]
    if lotto == side_reward1 or lotto == side_reward2:
        total += 100000
    # print(side_reward1, side_reward2)
    print(total)
main()
