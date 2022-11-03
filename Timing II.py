""" Timing II """

def main():
    """ return DDDD:HH:MM:SS """
    start_here = int(input())
    second = start_here
    minutes = second // 60
    second %= 60
    hour = minutes // 60
    minutes %= 60
    days = hour // 24
    hour %= 60
    print(days, hour, minutes, second)
main()
