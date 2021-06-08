import random
import math

char_1 = 'qwertyuıopğüasdfghjlşizxcvbnmöç'
char_2 = '1234567890'
char_3 = '!^+%&/()=?_-,;:.#${[]}\\|@'


class Muhammed:
    def Muhammed_iptal(**param):
        return 'işlem iptal edildi'

    def Muhammed_bosluk(**param):
        return ('\n' +' '*8 +'-' * 40 + '\n')

    def Muhammed_request(**param):
        var_muhammed = """
        ++++++++++++++++++++++++++++++
        | num | Türler               |
        |+++++|++++++++++++++++++++++|
        |  1  | sadece küçük harf    |
        |  2  | büyük  küçük harf    |
        |  3  | rakam ve harf        |
        |  4  | rakam harf noktalama |
        |+++++|++++++++++++++++++++++|
        ++++++++++++++++++++++++++++++
        """
        return var_muhammed

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
    system_run = True
    print(Muhammed.Muhammed_1())
    print(Muhammed.Muhammed_bosluk())
    print(Muhammed.Muhammed_request())
    while system_run:
        pusat = input('Şifre Güvenlik Düzeyi Seçiniz :\n> ')
        if str(pusat) == '1':
            print('1 Numaralı işlem seçildi')
        elif str(pusat) == '2':
            print('2 Numaralı işlem seçildi')
        elif str(pusat) == '3':
            print('3 Numaralı işlem seçildi')
        elif str(pusat) == '4':
            print('4 Numaralı işlem seçildi')
        else:
            print(' '*8+'Tanımlanayan komut > komutlar')
            print(Muhammed.Muhammed_request())
