""" RockPaperScissor """
def score_checker(result):
    """ check who the winner is"""
    if result[0] == result[1]:
        return ""
    else:
        if result == "RS" or result == "SP" or result == "PR":
            return "1"
        else:
            return "2"
def main():
    """ print final score """
    all_result = input()
    collector = ""
    for count in range(0, len(all_result), 2):
        collector += score_checker(all_result[count:count+2])
    p1_score = collector.count("1")
    p2_score = collector.count("2")
    if p1_score == p2_score:
        print("DRAW", p1_score)
    elif p1_score > p2_score:
        print("A win %d-%d"%(p1_score, p2_score))
    else:
        print("B win %d-%d"%(p2_score, p1_score))
main()
