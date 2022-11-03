""" BreachTheDoor """
def main(text):
    """ print > 6 letters """
    check = '0123456789\'"[]{}()!@#$%^&*_+;:?,.'
    for i in check:
        text = text.replace(i, "")
    text_list = text.split()
    text_list = list(filter(lambda var: len(var) > 6, text_list))
    print(" ".join(text_list))
main(input())
