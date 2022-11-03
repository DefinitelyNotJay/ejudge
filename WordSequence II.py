""" WordSequence II """
def main():
    """ print TRANSFORMER """
    text_1 = input()
    text_2 = input()
    result = ""
    for num in range(len(text_1)+1):
        result = text_2[:num] + text_1[num:]
        print(result)
    while len(result) != len(text_2):
        result = result + text_2[-(len(text_2)-len(result))]
        print(result)
main()
