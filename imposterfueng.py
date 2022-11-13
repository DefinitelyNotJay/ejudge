""" Impostor """
import json
def main():
    """ Impostor """
    player = dict()
    out = list()
    count = 0
    while True:
        text = input()
        if text == "Start":
            break
        cutplayer = json.loads(text)
        player.update(cutplayer)
        ansplayer = sorted(player)
    while True:
        txt = input()
        if txt == "End":
            break
        out.append(txt)
    for i in player:
        if i not in out:
            if player[i] == "Impostor":
                count += 1
    print(count,"Impostor Remains\n***Alive***")
    for j in ansplayer:
        if j not in out:
            print(j, player[j], sep=" : ")
    print("***Dead***")
    for k in ansplayer:
        if k in out:
            print(k, player[k], sep=" : ")
main()