""" LetterFrequency """
def main():
    """ print letter frequency """
    message = input().replace(" ", "").replace(".", '').lower()
    letter_dict = {}
    for alp in message:
        if alp in letter_dict:
            letter_dict[alp] += 1
        else:
            letter_dict[alp] = 1
    sorted_letter = sorted(letter_dict.items(), key=lambda var: -var[1])
    print(sorted_letter[0][0])
main()
