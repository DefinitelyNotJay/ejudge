""" Future Message """

def main():
    """ I'm on my way driving at 90 down those country lanes """
    text = input()
    if text.isnumeric() == True:
        print("Number")
    else:
        if text.isspace() == True:
            print("Space")
        elif text.istitle() == True:
            print("Title")
        elif text.isupper() == True:
            print("Uppercase")
        elif text.islower() == True:
            print("Lowercase")
        else:
            print("Other")
main()
