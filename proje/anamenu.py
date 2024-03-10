import hesaplamalar.hesap
import hesaplamalar.yas
import hesaplamalar.dersler
import hesaplamalar.para
import hesaplamalar.sn
import hesaplamalar.cizim
import hesaplamalar.pacman
def anamenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Hesap Makinesi                   ║")
    print("║        2:yaş hesabı                       ║")
    print("║        3:dersler                          ║")
    print("║        4:para kurları                     ║")
    print("║        5:sınav notları                    ║")
    print("║        6:çizim                            ║")
    print("║        7:pacman                           ║")
    print("║        8:                                 ║")
    print("║        9:                                 ║")
    print("║        10:                                ║")
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
        hesaplamalar.pacman.pacmenu()
        input()
        anamenu()
    if secim == "8":
        hesaplamalar.yas.ymenu()
        input()
        anamenu()   
    if secim == "9":
        hesaplamalar.yas.ymenu()  
        input()
        anamenu()
    if secim == "10":
        hesaplamalar.yas.ymenu()
        input()
        anamenu()   
    input()
anamenu()
