""" Matrix_MN """
def main(row, col):
    """ print MATRIX """
    matrix = [int(input()) for _ in range(row*col)]
    for count in range(1, row+1):
        print(*(matrix[(count-1)*col:col*count]))
main(int(input()), int(input()))
