""" BookWorm """
def worms_clan_wars():
    """ print IIT """
    for _ in range(int(input())):
        minutes = abs(float(input()))
        time_per_book = []
        for _ in range(abs(int(input()))):
            time_per_book.append(abs(float(input())))
        count, total = 0, 0
        time_per_book.sort()
        for time in time_per_book:
            if total+time <= minutes:
                total += time
                count += 1
            else:
                break
        print(count)
worms_clan_wars()