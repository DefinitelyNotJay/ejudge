""" Seeker """
def main():
    """ print seeker """
    number = []
    text = input()
    txt = ""
    for ch_ar in range(len(text)):
        if text[ch_ar].isdigit():
            txt += text[ch_ar]
        else:
            number.append(int(txt))
    print(sum(number))
main()
