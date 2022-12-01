"""GramV1s"""
def main():
    """ Step into your skin """
    text = input()
    lis = []
    string_builder = ""
    value = -1
    for i in range(len(text)-1):
        lis.append(text[i]+text[i+1])
    for i in lis:
        if lis.count(i) > value:
            string_builder = i
            value = lis.count(i)
    print(string_builder)
    print(value)
main()
