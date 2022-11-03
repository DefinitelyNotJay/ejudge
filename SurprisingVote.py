""" SurprisingVote """

def main():
    """ print surprising or not xD """
    total_score = float(input())
    highest_rate = float(input())
    left_rate = (total_score - highest_rate) / 2
    different = abs(highest_rate - left_rate)
    if different > 2.0:
        print("Surprising")
    else:
        print("Not surprising")
main()
