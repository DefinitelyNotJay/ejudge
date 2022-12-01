"""ClockHands"""
def main():
    """ https://www.youtube.com/watch?v=gEXfVi7wit8 """
    hour = int(input())
    seconds = int(input())
    hour *= 5
    hour += seconds / 12
    hour %= 60
    print(seconds <= hour < seconds+1)
main()
