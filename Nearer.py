"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    dis_alice = abs(icecream - alice)
    dis_bob = abs(icecream - bob)
    if dis_alice == dis_bob:
        print("Sundaes", dis_alice)
    elif dis_alice < dis_bob:
        print("Alice", dis_alice)
    else:
        print("Bob", dis_bob)
main()
