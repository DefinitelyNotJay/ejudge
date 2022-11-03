""" Filter """
import json
def main():
    """ print filtered score """
    details = json.loads(input())
    min_score = float(input())
    delete = []
    for key, value in details.items():
        if value < min_score:
            delete.append(key)
    for deleter in delete:
        details.pop(deleter)
    if len(details) == 0:
        print('Nope')
    else:
        details = sorted(details.items(), key=lambda var: int(var[0]))
        for key, value in details:
            print(key+"\t"+"%.2f"%(value))
main()
