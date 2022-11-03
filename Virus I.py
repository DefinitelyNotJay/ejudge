""" Virus I """
def main():
    """ print virus """
    txt = input()
    count = 0
    for virus in txt:
        if virus == 'o':
            count += 1
    print(count)
main()
