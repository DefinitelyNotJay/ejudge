""" Robot I """

def main():
    """ return permission """
    text = ""
    name = input("")
    age = float(input())
    if age < 18:
        text += ", you can pass."
    else:
        text += ", you shall not pass."
    print("%s%s"%(name, text))
main()
