""" CuteCat CuteFox """
def catcat(times):
    """ I'm not giving it up again """
    pets_collector = {}
    for _ in range(times):
        each_pet = input()
        if len(each_pet.split('"')) > len(each_pet.split("'")):
            pets_collector[each_pet.split('"')[1]] = each_pet.split('"')[3]
        else:
            pets_collector[each_pet.split("'")[1]] = each_pet.split("'")[3]
    cat, fox = 0, 0
    if "Cat01" not in pets_collector.values() and "Garfield" not in pets_collector:
        pets_collector.update({"Garfield" : "Cat01"})
    if "Fox01" not in pets_collector.values() and "Fubuki" not in pets_collector:
        pets_collector.update({"Fubuki" : "Fox01"})
    for criteria in pets_collector.values():
        if "Cat" in criteria:
            cat += 1
        elif "Fox" in criteria:
            fox += 1
    pets_collector = sorted(pets_collector.items(), key=lambda var: (var[1][:3], int(var[1][3:])))
    print("Cat : %i\nFox : %i"%(cat, fox))
    for ans in pets_collector:
        print(ans[0], ':', ans[1])
catcat(int(input()))
