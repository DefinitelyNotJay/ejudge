""" Caesar1 """
def main(roll, text):
    """ rolling in the deep """
    small_lets = [chr(var) for var in range(97, 123)]
    capital_lets = list(map(lambda var: var.upper(), small_lets))
    result = ""
    for i in text:
        if not(i in small_lets or i in capital_lets):
            result += i
        else:
            num = ord(i) + roll%26 - (97 if i in small_lets else 65)
            num -= 26 if num > 25 else 0
            result += small_lets[num] if i in small_lets else capital_lets[num]
    print(result)
main(int(input()), input())
