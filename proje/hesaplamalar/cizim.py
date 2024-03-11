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
        turtle.right (120)
        turtle.forward (f)
        turtle.right (120)
        turtle.forward (f)
        turtle.right (120)  
    if a == 5: 
        g = int(input("ikizkenar üçgeninizin ilk kenarını girin: "))
        j = int(input("ikizkenar üçgeninizin ikinci kenarını girin: "))
        i = int(input("üçgenin ilk açısını  girin: "))
        p = int(input("üçgenin ikinci açısını  girin: "))
        turtle.forward (g)
        turtle.right (i)
        turtle.forward (g)
        turtle.right (i)
        turtle.forward (j)
        turtle.right (p) 
    if a == 6: 
        n = int(input("çeşitkenar üçgeninizin 1. açısını girin: "))
        o = int(input("çeşitkenar üçgeninizin 2. açısını girin: "))
        p = int(input("çeşitkenar üçgeninizin 3. açsını girin: "))
        k = int(input("çeşitkenar üçgeninizin 1. kenarını girin: "))
        l = int(input("çeşitkenar üçgeninizin 2. kenarını girin: "))
        m = int(input("çeşitkenar üçgeninizin 3. kenarını girin: "))
        turtle.forward (k)
        turtle.right (n)
        turtle.forward (l)
        turtle.right (o)
        turtle.forward (m)
        turtle.right (p) 


        

    