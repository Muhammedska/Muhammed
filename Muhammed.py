import random
import math

char_1 = 'qwertyuıopğüasdfghjlşizxcvbnmöç'
char_2 = '1234567890'
char_3 = '!^+%&/()=?_-,;:.#${[]}\\|@'


class Muhammed:
    def Muhammed_iptal(**param):
        print('işlem iptal edildi')
    
    def Muhammed_1(**param):
        var_muhammed = """
        ###### ######  |  #    # | #
        #     #     #  |   #  #  | #
        #     #     #  |    ##   | #
        #     #     #  |   #  #  | # 
        #     #     #  |  #    # | ########

        version : 1.15.11
        yayıncı : Muhammed

        """
        return var_muhammed

    def Muhammed_x_1(**param):
        muhammed_run = True
        while muhammed_run:
            question = str(input('Karakter Sayısı Giriniz :\n> '))
            if type(question) == 'int':
                break
            elif question == '.iptal':
                muhammed_run = False
                return Muhammed.Muhammed_iptal()
            else:
                print('Lütfen Rakam Giriniz : \n işlem iptali için .iptal yazınız')


if __name__ == "__main__":
    print(Muhammed.Muhammed_1())
