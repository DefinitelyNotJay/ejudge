""" Seeker """
def main():
    """ seeker """
    ans = 0
    text = input()
    txt = ""
    for alp in text:
        if alp.isdigit():
            txt += alp
        else:
            if txt != "":
                ans += int(txt)
                txt = ""
            else:
                txt = ""
    print(ans+int(txt) if txt.isdigit() else ans)
main()
