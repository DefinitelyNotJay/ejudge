""" Digit v2 """
def main():
    """ 1212312121 """
    text = input()
    if 'thousand' in text:
        print(4)
    elif 'hundred' in text:
        print(3)
    elif 'ty' in text or 'twelve' in text or 'en' in text:
        print(2)
    else:
        print(1)
main()
