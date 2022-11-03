"""GraderMachine"""
def main():
    """GraderMachine"""
    first_num = int(input())
    last_num = int(input())
    sum = 0
    if first_num%2 != 0:
        first_num += 1
    if first_num >= 0 and last_num >=0:
        for ans in range(first_num, last_num+1, 2):
            sum = sum+ans
            if ans == first_num:
                print("pass : ", end="") 
                print(ans, end=" ")
            else:
                print(ans, end=" ")
    else:
        for ans in range(first_num, last_num-1, -2):
            sum = sum+ans
            if ans == first_num:
                print("pass : ", end="") 
                print(ans, end=" ")
            else:
                print(ans, end=" ")
    print("\nSum : %d" %sum)
main()