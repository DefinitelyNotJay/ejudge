""" Align """
def main():
    """ print aligned text """
    size = int(input())
    options = input().lower()
    text = input()
    space = " " * (size - len(text))
    result = ""
    if options == "center":
        if len(text) % 2 != 0:
            result += " "+text.center(size-1)
        else:
            result += text.center(size)
    elif options == "left":
        result += text + space
    elif options == "right":
        result += space + text
    print(result)
main()
