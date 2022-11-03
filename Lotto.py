""" Lotto """
def main():
    """ I still waiting my mom for winning some lottos """
    winner = input()
    last_2 = input()
    first1_3 = input()
    first2_3 = input()
    last1_3 = input()
    last2_3 = input()
    lotto = input()
    total = 0
    if lotto == winner:
        total += 6000000
    if lotto[-2:] == last_2:
        total += 2000
    if lotto[:4] != first1_3 and lotto[:4] != first2_3:
        total += 0
    elif lotto[:4] == first1_3 and lotto[:4] == first2_3:
        total += 8000
    else:
        total += 4000
    if lotto[-3:] != last1_3 and lotto[-3:] != last2_3:
        total += 0
    elif lotto[-3:] == last1_3 and lotto[-3:] == last2_3:
        total += 8000
    else:
        total += 4000
    if winner == '999999':
        side_reward1 = '000000'
    else:
        side_reward1 = str(int(winner) + 1)
    if winner == '000000':
        side_reward2 = '999999'
    else:
        side_reward2 = str(int(winner) - 1)
    if len(side_reward1) != 6 or len(side_reward2):
        side_reward1 = "0"*(4-len(side_reward1)) + str(side_reward1)[-len(side_reward1):]
        side_reward2 = "0"*(4-len(side_reward2)) + str(side_reward2)[-len(side_reward2):]
    if lotto == side_reward1 or lotto == side_reward2:
        total += 100000
    print(total)
main()
