"""[Recommend] iPhone 13 Again"""
def main():
    """iPhone 13 Again"""
    model = input()
    capacity = input()
    result = ""
    case1 = capacity == '128 GB' or capacity == '256 GB' or capacity == '512 GB'
    case2 = capacity == '128 GB' or capacity == '256 GB' or \
        capacity == '512 GB' or capacity == '1 TB'
    if (model == "iPhone 13 mini" or model == "iPhone 13") and case1:
        capacity = int(capacity[0:3])
        capacity = capacity // 128
        if model == "iPhone 13":
            result += str(29900 + 4000*(capacity-1))
        else:
            result += str(25900 + 4000*(capacity-1))
    elif (model == "iPhone 13 Pro" or model == "iPhone 13 Pro Max") and case2:
        if capacity == "1 TB":
            capacity = 6
        else:
            capacity = int(capacity[0:3])//128
        if model == "iPhone 13 Pro":
            result += str(38900 + 4000*(capacity-1))
        else:
            result += str(42900 + 4000*(capacity-1))
    else:
        result += "Not Available"
    print(result)
main()
