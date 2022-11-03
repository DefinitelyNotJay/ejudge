""" Key """

def main():
    """ print code lub lub krai ja roo🤫 """
    id_card = input()
    case_1 = 0
    for number in id_card:
        case_1 += int(number)
    # print(case_1)
    case_2 = int(id_card[-3] + id_card[-2] + id_card[-1]) * 10
    # print(case_2)
    key = str(case_1 + case_2)
    # print(key)
    if len(key) < 4:
        print(int(key)+1000)
    else:
        print(key[-4:])
main()
