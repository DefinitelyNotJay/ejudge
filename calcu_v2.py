"""hhh"""
def main(txt):
    """jj"""
    special_char = ",.?:;0123456789"
    for i in special_char:
        txt = txt.replace(i, "")
main(input())
