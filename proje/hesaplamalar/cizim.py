import turtle
def cizmenu():
    print("╔═══════════════════════════════════════════╗")
    print("║              Çizim Menüsü                 ║")
    print("║        1:Kare                             ║")
    print("║        2:Daire                            ║")
    print("║        3:Dikdörtgen                       ║")
    print("║        4:Eşkenar Üçgen                    ║")
    print("║        5:İkizkenar Üçgen                  ║")
    print("║        6:Çeşitkenar Üçgen                 ║")
    print("╚═══════════════════════════════════════════╝")
    a = int(input("tercihini gir : "))
    if a == 1: 
        b = int(input("karenin bir kenarını gir : "))
        turtle.forward (b)
        turtle.right (90)
        turtle.forward (b)
        turtle.right (90)
        turtle.forward (b)
        turtle.right (90)
        turtle.forward (b)
        turtle.right (90)
    if a == 2: 
        c = int(input("Dairenin yarıçapını girin: "))
        turtle.circle(c) 
    if a == 3: 
        d = int(input("Diktörtgenin ilk kenarını  girin: "))
        e = int(input("Diktörtgenin ikinci kenarını  girin: "))
        turtle.forward (d)
        turtle.right (90)
        turtle.forward (e)
        turtle.right (90)
        turtle.forward (d)
        turtle.right (90)
        turtle.forward (e)
        turtle.right (90) 
    if a == 4: 
        f = int(input("eşkenar üçgeninizin kenarını girin: "))
        turtle.forward (f)
        turtle.right (60)
        turtle.forward (f)
        turtle.right (60)
        turtle.forward (f)
        turtle.right (60)  


        

    