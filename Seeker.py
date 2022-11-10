""" Seeker """
def main():
    """ print seeker """
    total = 0
    text = input()
    txt = ""
    for alp in text:
        if alp.isdigit():
            txt += alp
        else:
            if txt != "":
                total += int(txt)
                txt = ""
            else:
                txt = ""
    print(total+int(txt) if txt.isdigit() else total)
main()
