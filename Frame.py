""" Frame """

def main():
    """ print text with flexible frame """
    text = input()
    top_and_bottom = "*" * int(len(text) + 2)
    print("%s\n*%s*\n%s"%(top_and_bottom, text, top_and_bottom))
main()
