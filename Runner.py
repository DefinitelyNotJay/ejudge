""" Runner """
def main():
    """ print result """
    distance, lap = int(input()), int(input())
    info = []
    for _ in range(lap):
        val = list(map(int, input().split()))
        info.extend([val])
    primal_info = info.copy()
    info.sort(key=lambda var: (-((distance-var[1])/var[0]), var[0]))
    print(primal_info.index(info[-1])+1)
main()
