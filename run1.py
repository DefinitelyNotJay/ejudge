"""Run Length Encoding"""
def main(message):
    """find that result"""
    count = 0
    check = message[0]
    for i in message:
        if i == check:
            count += 1
        else:
            print(str(count) + check, end="")
            count = 1
            check = i
    print(str(count) + check, end="")
main(input())
