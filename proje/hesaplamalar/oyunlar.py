import hesaplamalar.pacman
import hesaplamalar.snake
import hesaplamalar.connect
import hesaplamalar.ping_pong
def oyunmenu():
    print("╔═══════════════════════════════════════════╗")
    print("║                  Ana Menü                 ║")
    print("║        1:Pacman                           ║")
    print("║        2:Snake                            ║")
    print("║        3:Connect                          ║")
    print("║        4:ping pong                        ║")
    print("╚═══════════════════════════════════════════╝")
    secim = (input(" tercihini gir "))
    if secim == "1":
        hesaplamalar.pacman.pacmenu()
        input()
        oyunmenu()
    if secim == "2":
        hesaplamalar.snake.smenu()
        input()
        oyunmenu()
    if secim == "3":
        hesaplamalar.connect.cmenu() 
        input()
        oyunmenu()
    if secim == "4":
        hesaplamalar.connect.omenu() 
        input()
        oyunmenu()