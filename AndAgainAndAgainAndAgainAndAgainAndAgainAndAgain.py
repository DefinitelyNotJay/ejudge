""" AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain """
def main():
    """ a e i o u """
    words = input().strip().split()
    words_result = words.copy()
    result = []
    for num in range(len(words)):
        fixed_word = words[num].replace('a', '#').replace('e', '#').replace('i', '#') \
        .replace('o', '#').replace('u', '#')
        if fixed_word.count("#") > 1:
            result.append(words_result[num].replace('.', ''))
    if len(result) > 0:
        result.sort()
        print("\n".join(result))
    else:
        print("Nope")
main()
