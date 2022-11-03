""" DataSpike """
 
def find_most_value(most_value):
    """ return most value """
    num = int(input())
    if num > most_value:
        return num
    else:
        return most_value
 
def main():
    """ print most() but this one cannot use :'( """
    most_value = 0
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    most_value = find_most_value(most_value)
    print(most_value)
main()