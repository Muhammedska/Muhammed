import random
import math

char_1 = 'qwertyuıopğüasdfghjlşizxcvbnmöç'
char_2 = '1234567890'
char_3 = '!^+%&/()=?_-,;:.#${[]}\\|@'
char_4 = char_1.upper()

class Muhammed:
    def Muhammed_cancel(**param):
        return 'işlem iptal edildi'

    def Muhammed_space(**param):
        return ('\n' + ' ' * 8 + '-' * 40 + '\n')

    def Muhammed_request(**param):
        var_muhammed = """
        ++++++++++++++++++++++++++++++
        | num | Türler               |
        |+++++|++++++++++++++++++++++|
        |  0  | Çıkış yapmak için    |
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
            try:
                question = int(input('Karakter Sayısı Giriniz [min 8 karakter giriniz] :\n> '))
                if question == 0:
                    print(Muhammed.Muhammed_cancel() + Muhammed.Muhammed_space())
                    break

                elif question >= 8:
                    var_pass = ''
                    var_counter = 0
                    var_charlist = []
                    for i in char_1:
                        var_charlist.append(i)
                    for i in range(0, question):
                        var_pass += random.choice(var_charlist)
                    pretty_pass = '+' * (
                                len(var_pass) + 4 + len('output') + 3) + '\n| output | ' + var_pass + ' |\n' + '+' * (
                                              len(var_pass) + 4 + len('output') + 3)
                    print('\n' + pretty_pass + '\n')
                    muhammed_run = False
                else:
                    print('Lütfen 8 ve 8 den büyük rakam giriniz :\n')
            except ValueError:
                print("Sadece sayı giriniz lütfen... | çıkış için ' 0 ' rakamını giriniz.\n")

    def Muhammed_x_2(**param):
        muhammed_run = True
        while muhammed_run:
            try:
                question = int(input('Karakter Sayısı Giriniz [min 8 karakter giriniz] :\n> '))
                if question == 0:
                    print(Muhammed.Muhammed_cancel() + Muhammed.Muhammed_space())
                    break

                elif question >= 8:
                    var_pass = ''
                    var_counter = 0
                    var_charlist_all = []
                    var_charlist_1 = []
                    var_charlist_2 = []
                    var_pass_list = []

                    for i in char_1:
                        var_charlist_1.append(i)
                        var_charlist_all.append(i)

                    for i in char_4:
                        var_charlist_2.append(i)
                        var_charlist_all.append(i)

                    for i in range(0, question):
                        var_pass_list.append(random.choice(var_charlist_all))
                        random.shuffle(var_pass_list)

                    for i in var_pass_list:
                        var_pass += i

                    pretty_pass = '+' * (
                                len(var_pass) + 4 + len('output') + 3) + '\n| output | ' + var_pass + ' |\n' + '+' * (
                                              len(var_pass) + 4 + len('output') + 3)
                    print('\n' + pretty_pass + '\n')
                    muhammed_run = False
                else:
                    print('Lütfen 8 ve 8 den büyük rakam giriniz :\n')
            except ValueError:
                print("Sadece sayı giriniz lütfen... | çıkış için ' 0 ' rakamını giriniz.\n")

    def Muhammed_x_3(**param):
        muhammed_run = True
        while muhammed_run:
            try:
                question = int(input('Karakter Sayısı Giriniz [min 8 karakter giriniz] :\n> '))
                if question == 0:
                    print(Muhammed.Muhammed_cancel() + Muhammed.Muhammed_space())
                    break

                elif question >= 8:
                    var_pass = ''
                    var_counter = 0
                    var_charlist_all = []
                    var_charlist_1 = []
                    var_charlist_2 = []
                    var_pass_list = []

                    for i in char_1:
                        var_charlist_1.append(i)
                        var_charlist_all.append(i)

                    for i in char_2:
                        var_charlist_2.append(i)
                        var_charlist_all.append(i)

                    for i in range(0, question):
                        var_pass_list.append(random.choice(var_charlist_all))
                        random.shuffle(var_pass_list)

                    for i in var_pass_list:
                        var_pass += i

                    pretty_pass = '+' * (
                            len(var_pass) + 4 + len('output') + 3) + '\n| output | ' + var_pass + ' |\n' + '+' * (
                                          len(var_pass) + 4 + len('output') + 3)
                    print('\n' + pretty_pass + '\n')
                    muhammed_run = False
                else:
                    print('Lütfen 8 ve 8 den büyük rakam giriniz :\n')
            except ValueError:
                print("Sadece sayı giriniz lütfen... | çıkış için ' 0 ' rakamını giriniz.\n")

    def Muhammed_x_4(**param):
        muhammed_run = True
        while muhammed_run:
            try:
                question = int(input('Karakter Sayısı Giriniz [min 8 karakter giriniz] :\n> '))
                if question == 0:
                    print(Muhammed.Muhammed_cancel() + Muhammed.Muhammed_space())
                    break

                elif question >= 8:
                    var_pass = ''
                    var_counter = 0
                    var_charlist_all = []
                    var_charlist_1 = []
                    var_charlist_2 = []
                    var_charlist_3 = []
                    var_charlist_4 = []
                    var_pass_list = []

                    for i in char_1:
                        var_charlist_1.append(i)
                        var_charlist_all.append(i)

                    for i in char_2:
                        var_charlist_2.append(i)
                        var_charlist_all.append(i)

                    for i in char_3:
                        var_charlist_3.append(i)
                        var_charlist_all.append(i)

                    for i in char_4:
                        var_charlist_3.append(i)
                        var_charlist_all.append(i)

                    for i in range(0, question):
                        random.shuffle(var_charlist_all)
                        var_pass_list.append(random.choice(var_charlist_all))
                        random.shuffle(var_pass_list)

                    for i in var_pass_list:
                        var_pass += i

                    pretty_pass = '+' * (
                                len(var_pass) + 4 + len('output') + 3) + '\n| output | ' + var_pass + ' |\n' + '+' * (
                                              len(var_pass) + 4 + len('output') + 3)
                    print('\n' + pretty_pass + '\n')
                    muhammed_run = False
                else:
                    print('Lütfen 8 ve 8 den büyük rakam giriniz :\n')
            except ValueError:
                print("Sadece sayı giriniz lütfen... | çıkış için ' 0 ' rakamını giriniz.\n")


if __name__ == "__main__":
    system_run = True
    print(Muhammed.Muhammed_1())
    print(Muhammed.Muhammed_space())
    print(Muhammed.Muhammed_request())
    while system_run:
        pusat = input('Şifre Güvenlik Düzeyi Seçiniz :\n> ')
        if str(pusat) == '0':
            print('Çıkış İşlemi Seçildi')
            input('kapatmak için enter basınız')
            system_run = False
        elif str(pusat) == '1':
            print('1 Numaralı işlem seçildi\n')
            Muhammed.Muhammed_x_1()
        elif str(pusat) == '2':
            print('2 Numaralı işlem seçildi\n')
            Muhammed.Muhammed_x_2()
        elif str(pusat) == '3':
            print('3 Numaralı işlem seçildi\n')
            Muhammed.Muhammed_x_3()
        elif str(pusat) == '4':
            print('4 Numaralı işlem seçildi\n')
            Muhammed.Muhammed_x_4()
        else:
            print(' ' * 8 + 'Tanımlanayan komut > komutlar')
            print(Muhammed.Muhammed_request())
