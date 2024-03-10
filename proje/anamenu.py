import hesaplamalar.hesap
import hesaplamalar.yas
import hesaplamalar.dersler
import hesaplamalar.para
def anamenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Hesap Makinesi                   ║")
    print("║        2:yaş hesabı                       ║")
    print("║        3:dersler                          ║")
    print("║        4:para kurları                     ║")
    print("║        5:sınav notları                    ║")
    print("║        6:                                 ║")
    print("║        7:                                 ║")
    print("║        8:                                 ║")
    print("║        9:                                 ║")
    print("║        10:                                ║")
    print("╚═══════════════════════════════════════════╝")
    secim = (input(" tercihini gir "))
    if secim == "1":
        hesaplamalar.hesap.hmmenu()
    if secim == "2":
            hesaplamalar.yas.ymenu()
    if secim == "3":
            hesaplamalar.dersler.dersmenu ()
    if secim == "4":
            hesaplamalar.para.pmenu()
    if secim == "5":
            hesaplamalar.yas.ymenu()
    if secim == "6":
            hesaplamalar.yas.ymenu()
    if secim == "7":
            hesaplamalar.yas.ymenu()
    if secim == "8":
            hesaplamalar.yas.ymenu()   
    if secim == "9":
            hesaplamalar.yas.ymenu()  
    if secim == "10":
            hesaplamalar.yas.ymenu()   
    input()
anamenu()
