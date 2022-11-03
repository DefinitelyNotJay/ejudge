""" HideAndSeek """

def main():
    """ print defined number sequence"""
    starter = int(input())
    stopper = int(input())
    plus_value = int(input())
    for i in range(starter, stopper, plus_value):
        print(i)
main()
