""" [Recommend] BTSMRT ver.ทำแบบอาจารย์"""
def main():
    """ helping children or older in special day :o """
    date = input().title()
    age = abs(float(input()))
    height = abs(float(input()))
    case1 = date == "Children Day" and age < 14 and height <= 140
    case2 = age < 14 and height < 90
    case3 = date == "Senior Day" and age >= 60
    if case1 or case2 or case3:
        print("FREE")
    else:
        print("PAY")
main()
