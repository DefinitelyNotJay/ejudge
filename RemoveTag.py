""" RemoveTag """
def tagtag():
    """ print tag without <><> """
    text = input()
    while True:
        if text.find("<") != -1:
            text = text.replace(text[text.find("<"):text.find(">")+1], " ")
        else:
            break
    print(text.split())
tagtag()
