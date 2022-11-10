""" Seeker """
def main(text):
    """ print secret password """
    prev = ""
    collector = ""
    for i in range(len(text)):
        if text[i].isdigit():
            if text[i+1].isdigit():
                collect += i
            else:
                total += int(collect)

