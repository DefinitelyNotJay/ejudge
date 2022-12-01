""" Heads and Legs """
def main():
    """ Rainnyy loves noodles """
    total_animals = int(input())
    total_legs = int(input())
    rabbits = (total_legs-2*total_animals)//2
    ghost = (total_legs-2*total_animals)%2
    birds = total_animals - rabbits
    if rabbits >= 0 and birds >= 0 and ghost == 0:
        print(rabbits, birds)
    else:
        print("Impossible")
main()
