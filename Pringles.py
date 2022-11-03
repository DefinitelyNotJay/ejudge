""" Pringles """
def main():
    """ print pringles left """
    top = input()
    pieces = input()
    bot = input()
    num = int(input())
    cut = (len(top) + 1) - num
    full = pieces.count(")")
    pieces = " "*num + pieces[-(cut):]
    left = pieces.count(")")
    got_chip = abs(full - left)
    text = "There are still some left."
    if left == 0:
        text = "None."
    print(got_chip, text, top, pieces, bot, sep='\n')
main()
