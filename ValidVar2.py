"""ValidVar"""
def main():
    """print id's variable name if it's possible"""
    punctuation = "%$<>,.'\"/-=()[]{}^#@&;:ฺ|.~"
    restrict_word = ["if", "else", "elif", "while", "for", "True", "False", "continue", "break",\
    "return", "is", "in", "and", "or", "from", "as", "pass", "not", "def", "None", "class", "try",\
    "global", "with", "async", "yield", "nonlocal", "await", "except", "finally", "import", \
    "assert", "raise", "lambda"]
    num = int(input())
    case_1, case_2, case_3, case_4 = "", "", "", ""
    for _ in range(num):
        text = input()
        for special_char in punctuation:
            if text.find(special_char) != -1:
                case_1 += "wrong"
        for words in restrict_word:
            if words == text:
                case_2 += "wrong"
        for find_space in text[1:-1]:
            if find_space == " ":
                case_3 += 'wrong'
        if text.strip()[0].isnumeric() == True:
            case_4 += 'wrong'
        if case_1 == "" and case_2 == "" and case_3 == "" and case_4 == "":
            print("Valid")
        else:
            print("Invalid")
        case_1, case_2, case_3, case_4 = "", "", "", ""
main()
