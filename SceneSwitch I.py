""" SceneSwitch I """
def main():
    """ Go down
Soft sound
Midnight
Car lights
Playing with the air
Breathing in your hair
Go down
Soft sound
Step into your skin?
I'd rather jump in your bones
Taking up your mouth, so you breathe through your nose """
    times, prev, total = input(), 0, 0
    light, stat = "warm", "online"
    while times != "End":
        remain = abs(float(times) - float(prev))
        if stat == "online":
            stat = "offline"
            print("Con 1")
        elif (stat == "offline" and remain > 6) or light == "warm":
            light = "cool"
            stat = "online"
            print("Con 2")
        elif stat == "offline" and light == "cool":
            total += 1
            light = "warm"
            stat = "online"
            print("Con 3")
        prev = times
        times = input()
    print(total)
main()
