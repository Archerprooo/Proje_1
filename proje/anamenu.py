import hesaplamalar.hesap
import hesaplamalar.yas
import hesaplamalar.dersmenu
def anamenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Hesap Makinesi                   ║")
    print("║        2:yaş hesabı                       ║")
    print("║        3:dersler                          ║")
    print("║        4:içecekler                        ║")
    print("║        5:yiyecekler                       ║")
    print("║        6:bilgisayar markaları             ║")
    print("║        7:para birimleri                   ║")
    print("║        8:sınav notları                    ║")
    print("║        9:yararlı bitkiler                 ║")
    print("║        10:                                ║")
    print("╚═══════════════════════════════════════════╝")
    secim = (input(" tercihini gir "))
    if secim == "1":
        hesaplamalar.hesap.hmmenu()
    if secim == "2":
            hesaplamalar.yas.ymenu()
    if secim == "3":
            hesaplamalar.dersler.dersmenu()
    if secim == "4":
            hesaplamalar.yas.ymenu()
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
