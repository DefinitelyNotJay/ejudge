""" Kabata """
def main(lap):
    """ print unknown language """
    result = []
    for _ in range(lap):
        words = input()
        # katakabakakabakaka
        if "baka" in words:
            result.append("no")
        else:
            check = words.replace("bakka", " ").replace("ka", " ") \
            .replace("ba", " ").replace("ta", " ")
            if check.strip() == "":
                result.append("yes")
            else:
                result.append("no")
    print("\n".join(result))
main(int(input()))
