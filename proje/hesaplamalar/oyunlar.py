import hesaplamalar.pacman
def oyunmenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Pacman                           ║")
    print("║        2:                                 ║")
    print("║        3:                                 ║")
    print("║        4:                                 ║")
    print("╚═══════════════════════════════════════════╝")
    secim = (input(" tercihini gir "))
    if secim == "1":
        hesaplamalar.pacman.pacmenu()
        input()
        oyunmenu()
    if secim == "2":
   
        input()
        oyunmenu()
    if secim == "3":
        
        input()
        oyunmenu()
    if secim == "4":
       
        input()
        oyunmenu()