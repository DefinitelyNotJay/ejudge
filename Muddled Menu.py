""" Muddled Menu """
def main():
    """ print menu """
    menu = input()
    all_menu = []
    while menu != "DONE":
        if menu == 'CLOSED' or menu == "SOMETHING'S WRONG":
            all_menu.clear()
            if menu == 'CLOSED':
                break
        elif menu[:8] == "Can't do":
            all_menu.remove(menu[menu.rfind(':')+2:])
        else:
            menu = menu.split(" #")
            first = menu[0]
            second = menu[1]
            if second == 'N':
                all_menu.append(first)
            else:
                all_menu.insert(int(second)-1, first)
        menu = input()
    reversed_menu = all_menu.copy()
    reversed_menu.reverse()
    print("Full Course:", all_menu, "Reversed:", reversed_menu)
main()
