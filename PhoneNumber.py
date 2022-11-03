"""PhoneNumber"""
def main():
    """PhoneNumber"""
    num = input().strip()
    level = input()
    result = ''
    if level != 'Domestic':
        num = "+66" + num[1:]
    if level == 'Domestic':
        if len(num) == 10:
            result += num[:2] + " " + num[2:6] + " " + num[6:]
        else:
            result += num[0] + " " + num[1:5] + " " + num[5:]
    else:
        if len(num) == 11:
            result += num[:3] + " " + num[3:7] + " " + num[7:]
        else:
            result += num[:4] + " " + num[4:8] + " " + num[8:]
    print(result)
main()
