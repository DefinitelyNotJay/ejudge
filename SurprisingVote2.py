""" SurprisingVote """

def main():
    """print SURPRISE"""
    total_score = float(input())
    highest_score = float(input())
    left_score = 0
    if highest_score*2 < total_score:
        left_score = total_score - (highest_score*2)
    if highest_score - left_score > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
