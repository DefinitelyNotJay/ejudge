""" Flatten """
import json
def check(just_list):
    for cha in just_list:
        if not isinstance(cha, int):
            just_list.remove(cha)
        else:
            just_list.append(cha)


    print(cha, type(cha))
def main():
    """ main function """
    primal_list = json.loads(input())
    result = list()

    print(primal_list)
    print(result)
main()
