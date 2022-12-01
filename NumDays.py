""" NumDays """
def main():
    """ มีเด็กน้อยคนนึงตาจะปิดไม่ค่อยได้ลืม """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day1, month1 = int(input()), int(input())
    day2, month2 = int(input()), int(input())
    if month1 > month2:
        temp1 , temp2 = day1, month1
        day1, month1 = day2, month2
        day2, month2 = temp1, temp2
    con1 = 0 < day1 <= days[month1-1] and 0 < day2 <= days[month2-1]
    con2 = 0 < month1 < 13 and 0 < month2 < 13
    if con1 and con2:
        print(days[month1-1] - day1)
        total_days_1 = sum(days[:month1]) + day1 + (days[month1-1] - day1)
        total_days_2 = sum(days[:month2]) + day2

        total_days_1 += days[month1]
        print(total_days_1, total_days_2)
        print(abs(total_days_1-total_days_2))
    else:
        print("Impossible")
main()
