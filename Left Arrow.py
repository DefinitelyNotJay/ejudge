""" Left Arrow """
def main():
    """ print left arrow  """
    width = int(input())
    height = int(input())
    top = (height//2)+1
    left = height - top
    for row in range(1, top+1):
        for _ in range(top-row, 0, -1):
            print(" ", end="")
        for _ in range(width):
            print("*", end="")
        print()
    for row in range(1, left+1):
        for _ in range(1, row+1):
            print(" ", end="")
        for _ in range(width):
            print("*", end="")
        print()
main()
