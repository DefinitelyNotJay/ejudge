""" Impostor """
def main():
    """ AMONGUS """
    player, death, count = {}, {}, 0
    amount = input()
    while amount != 'Start':
        info = amount[1:-1].replace('"', "").split(" : ")
        player.update({info[0] : info[1]})
        amount = input()
    kill = input()
    while kill != 'End':
        death[kill] = player.pop(kill)
        kill = input()
    for left in player.values():
        if left == "Impostor":
            count += 1
    player = sorted(player.items(), key=lambda var: (var[0], var[1]))
    death = sorted(death.items(), key=lambda var: (var[0], var[1]))
    print(count, 'Impostor Remains\n***Alive***')
    for key, values in player:
        print(key, ":", values)
    print("***Dead***")
    for key, values in death:
        print(key, ":", values)
main()
