""" PlanB """

def main():
    """ return process result """
    score = float(input())
    text = ""
    if score >= 450:
        text += "Pass"
    else:
        text += "Fail"
    print(text)
    print("Process is terminated")
main()
