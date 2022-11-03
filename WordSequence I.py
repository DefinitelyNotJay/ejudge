""" WordSequence I """
def main():
    """ print stair """
    text = input()
    for num in range(1, len(text)+1):
        print(text[:num])
main()
