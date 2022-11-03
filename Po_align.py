"""Align"""
def main():
    """x"""
    size = int(input())
    place = input()
    txt = input()
    man_txt = len(txt)
    space = size-len(txt)
    if place == "left":
        print(txt+""*space)
    elif place == "right":
        print(txt.rjust(size))
    else:
        if man_txt%2 != 0:
            print(" "+txt.center(size-1))
        else:
            print(txt.center(size))
main()