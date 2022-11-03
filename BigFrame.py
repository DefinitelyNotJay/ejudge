""" BigFrame """
def main():
    """ print frame suay suay """
    all_text = [input(), input(), input(), input(), input()]
    len_text = [0, 0, 0, 0, 0]
    for i in range(len(all_text)):
        if all_text[i].isspace() != True:
            all_text[i] = all_text[i].strip()
        len_text[i] = len(all_text[i])
    max_width = max(len_text)
    print("*"*(max_width+4))
    for text in all_text:
        width = max_width - len(text)
        print("* %s%s *"%(text, " "*width))
    print("*"*(max_width+4))
main()
