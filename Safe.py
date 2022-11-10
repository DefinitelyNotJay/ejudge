""" Safeboys """
def main(word1, word2):
    """ Nothing happens until something moves """
    total = 0
    for alp1, alp2 in zip(word1, word2):
        alp1, alp2 = ord(alp1) - 64, ord(alp2) - 64
        if alp1 < alp2:
            alp1, alp2 = alp2, alp1
        normal_case = alp1 - alp2
        special_case = (26-alp1) + alp2
        if normal_case > special_case:
            total += special_case
        else:
            total += normal_case
    print(total)
main(input(), input())
