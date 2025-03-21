"""
**  BankaHesabi isminde bir sinif tanimlayiniz.
**  Uretilen her nesne "hesapSahibi" isminde bir ozelligi sahip olmalidir. BankaHesabi("Sadik Turan")
**  Uretilen her bir nesne "bakiye" isminde bir ozellige sahip olup baslangicta 0.0 degerinde olmalidir.
**  Uretilen her bir nesne icin "paraYatir" metodu olusturun ve disaridan yatirilacak miktar bilgisini 
    alip bakiye uzerine ekleyin ve bakiye miktarini geriye dondurun.
**  Uretilen her bir nesne icin "paraCek" metodu olusturun ve disaridan cekilen miktar bilgisini alip 
    bakiye degerinde cikarip geriye dondurun.

    hesap = BankHesabi("Sadik Turan")
    hesap.hesapSahibi => Sadik Turan
    hesap.bakiye => 0.0
    hesap.paraYatir(1000) => 1000.0
    hesap.paraCek(500) => 500.0
"""

class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0.0

    def get_bakiye(self):
        return self.bakiye
    
    def paraYatir(self, para):
        self.bakiye += para
        return self.bakiye
    
    def paraCek(self, para):
        self.bakiye -= para
        return self.bakiye
    

hesap = BankaHesabi("Sude Su")
print(hesap.paraYatir(1000))
print(hesap.get_bakiye())
hesap.paraCek(500)
print(hesap.get_bakiye())
hesap.paraCek(200)
print(hesap.get_bakiye())

