""" Turnstile """
def main():
    """ count all entering """
    all_action = ''
    while True:
        action = input()
        if action == 'END':
            break
        all_action += action
    print(all_action.count('CP'))
main()
