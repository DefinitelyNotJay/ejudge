"""Elo"""
def elo(first, second, option):
    """ return result """
    result = 0
    if option == "B":
        first, second = second, first
    result += 1/(1+10**((second-first)/400))
    return result

def main():
    """Elo"""
    first_score = int(input())
    second_score = int(input())
    output = input()
    print("%.2f"%elo(first_score, second_score, output))
main()
