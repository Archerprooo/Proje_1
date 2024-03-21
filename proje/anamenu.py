import hesaplamalar.hesap
import hesaplamalar.yas
import hesaplamalar.dersler
import hesaplamalar.para
import hesaplamalar.sn
import hesaplamalar.cizim
import hesaplamalar.oyunlar
import hesaplamalar.tvs
import hesaplamalar.ct
import hesaplamalar.rast
import turtle
import datetime
def anamenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Hesap Makinesi                   ║")
    print("║        2:yaş hesabı                       ║")
    print("║        3:dersler                          ║")
    print("║        4:para kurları                     ║")
    print("║        5:sınav notları                    ║")
    print("║        6:çizim                            ║")
    print("║        7:oyunlar                          ║")
    print("║        8:tarih ve saat                    ║")
    print("║        9:çarpım tablosu                   ║")
    print("║        10:rastgele sayı                   ║")
    print("╚═══════════════════════════════════════════╝")
    secim = (input(" tercihini gir "))
    if secim == "1":
        hesaplamalar.hesap.hmmenu()
        input()
        anamenu()
    if secim == "2":
        hesaplamalar.yas.ymenu()
        input()
        anamenu()
    if secim == "3":
        hesaplamalar.dersler.dersmenu ()
        input()
        anamenu()
    if secim == "4":
        hesaplamalar.para.pmenu()
        input()
        input()
        anamenu()
    if secim == "5":
        hesaplamalar.sn.nmenu()
        input()
        anamenu()
    if secim == "6":
        hesaplamalar.cizim.cizmenu()
        input()
        anamenu()
    if secim == "7":
        hesaplamalar.oyunlar.oyunmenu()
        input()
        anamenu()
    if secim == "8":
        hesaplamalar.tvs.tsv()
        input()
        anamenu()   
    if secim == "9":
        hesaplamalar.ct.ct()  
        input()
        anamenu()
    if secim == "10":
        hesaplamalar.rast.rast()
        input()
        anamenu()   
    input()
anamenu()
