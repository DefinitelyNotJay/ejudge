""" MAC """
def check_pos(text, check):
    """ check check """
    number = 1
    if check == ':':
        number = 2
    elif check == '.':
        number = 3
    text_inside = ""
    text_alphabet = ""
    for alp in text:
        if alp == check:
            text_inside += alp
        else:
            text_alphabet += alp
    if text_inside == "-----" or text_inside == ":::::" or text_inside == "..":
        return True, number
    else:
        return False, number
def main():
    """ print checked string """
    text = input().lower()
    con1 = text[2] == ":" or text[2] == "-"
    con2 = text[4] == "."
    con3 = False
    con4 = True
    case = "1"
    text_check = ""
    sp_char = ""
    if con1:
        sp_char = text[2]
        con3, case = check_pos(text, text[2])
    elif con2:
        sp_char = text[4]
        con3, case = check_pos(text, text[4])
    if con3 == True:
        for char in text:
            if not(97 <= ord(char) <= 122 or 48 <= ord(char) \
                <= 57 or ord(char) == ord(sp_char)):
                text += 'blah'
    if text_check != "":
        con4 = False
    if (con1 or con2) and con3 and con4:
        print("VALID", case)
    else:
        print("ERROR")
main()
