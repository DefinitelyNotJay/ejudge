"""Imposter"""
def main():
    """Imposter"""
    dead = []
    dict_alive = {}
    countt = 0
    while True:
        txt = input()
        if txt == "Start":
            break
        txt = txt[1:-1].replace('"', "").split(" : ")
        dict_alive[txt[0]] = txt[1]
        # dict[key] = value
    while True:
        out = input()
        if out == "End":
            break
        dead.append(out)
    full_player = dict_alive.copy()
    for i in dead:
        dict_alive.pop(i)

    for val in dict_alive.values():
        if val == "Impostor":
            countt +=1
    dict_alive = sorted(dict_alive.items())
    print(countt, "Impostor Remains")
    print("***Alive***")
    # ไอ้เจสอนไรวะสัส
    for j, k in dict_alive:
        print(j, ":", k)
    print("***Dead***")
    for name in sorted(dead):
        print(name, ":", full_player[name])
main()
