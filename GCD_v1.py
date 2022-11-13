"""
                      (`.-,\')
                    .-'     ;
                _.-'   , `,-
          _ _.-'     .'  /._
        .' `  _.-.  /  ,'._;)
       (       .  )-| (
        )`,_ ,'_,'  \\_;)
('_  _,'.'  (___,))
 `-:;.-'
"""
def main():
    """ print GCD """
    num1, num2 = int(input()), int(input())
    while num2:
        num1, num2 = num2, num1%num2
    print(num1)
main()
