""" Ping """
def calculate(packet, most, least, total):
    """ just calculate """
    time = packet.find("time")
    millisec = packet.find('ms')
    if time != -1 and millisec != -1:
        num = int(packet[time+5:millisec])
        if packet.find("<") != -1:
            num = 0
        return max(num, most), min(num, least), total+num
    return most, least, total
def main():
    """ print required data """
    first_line = input()
    _ = input()
    ip_add = input()
    if "[" in ip_add:
        ip_add = ip_add[ip_add.find("[")+1:ip_add.find("]")]
    else:
        ip_add = first_line[first_line.find('ping')+5:]
    packet1, packet2, packet3, packet4 = input(), input(), input(), input()
    receive = (packet1 + packet2 + packet3 + packet4).count("Reply from")
    lost = 4 - receive
    percent = int(100*lost/4)
    if receive == 0:
        percent = 100
    most, least, total = 0, 9999, 0,
    most, least, total = calculate(packet1, most, least, total)
    most, least, total = calculate(packet2, most, least, total)
    most, least, total = calculate(packet3, most, least, total)
    most, least, total = calculate(packet4, most, least, total)
    print("Ping statistics for %s:"%ip_add)
    print("    Packets: Sent = %s, Received = %d, Lost = %d (%s loss),\
        "%(4, receive, lost, str(percent)+"%"))
    if receive != 0:
        print("Approximate round trip times in milli-seconds:\n\
    Minimum = %dms, Maximum = %dms, \
Average = %dms"%(least, most, int(total/receive)))
main()
