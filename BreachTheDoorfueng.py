""" BreachTheDoor """
def main():
    """ BreachTheDoor """
    txt = input()
    restic = "0123456789'/<>,.?()-+*&^%$#@:!;=\ฺ{\}_~[]"
    anslist = []
    for i in restic:
        txt.replace(i, "")
    anslist.append(txt)
    print(anslist)
            
main()