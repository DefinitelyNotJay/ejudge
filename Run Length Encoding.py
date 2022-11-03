""" Run Length Encoding """

def main():
    """ print changed password """
    text = input()
    collector = []
    each_al = ""
    result = ""
    count = ""
    if len(text) > 1:
        for jay in range(len(text)-1):
            if text[jay] == text[jay+1]:
                each_al += text[jay]
            else:
                each_al += text[jay]
                collector.append(each_al)
                each_al = ""
            count = str(jay)
        # บวกชุดสุดท้ายเข้าไป
        jay = int(count)
        each_al += text[jay+1]
        collector.append(each_al)
        for k in range(len(collector)):
            result += str(len(collector[k]))
            result += str(collector[k][0])
    else:
        result += "1%s"%text
    print(result)
main()
