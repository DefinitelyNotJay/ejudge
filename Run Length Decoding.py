""" Run Length Decoding """
def main():
    """ print decoded password """
    text = input()
    result = ""
    for i in range(len(text)):
        if ord(text[i]) > 65:
            result += text[i]
            temp = len(result) - 1
            print(int(result[:temp])*result[-1], end="")
            result = ""
        else:
            result += text[i]
main()
