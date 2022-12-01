""" BloodDonation """
def main():
    """ Go down soft sound """
    age = int(input())
    weight = int(input())
    times = int(input())
    con1 = 17 <= age <= 70
    con2 = weight >= 45
    con3 = False if times == 0 and age > 55 else True
    con5 = True
    if age == 17 or (age >= 60 and age <= 70):
        permit = input()
        con5 = False if permit == 'False' else True
    con4 = False if age == 17 and permit == "False" else True
    if con1 and con2 and con3 and con4 and con5:
        print("Yes")
    else:
        print("No")
main()
