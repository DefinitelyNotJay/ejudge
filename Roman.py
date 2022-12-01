""" givin' up givin' up again """
def roman(text):
    """ NEW 1-0 CHE the pain must go on """
    total = 0
    roman_dict = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50,\
"X" : 10, "V" : 5, "I" : 1}
    i = len(text) - 1
    while i >= 0:
        if i != len(text)-1 and roman_dict[text[i]] < roman_dict[text[i+1]]:
            total -= roman_dict[text[i]]
        else:
            total += roman_dict[text[i]]
        i -= 1
    print(total)
roman(input())
