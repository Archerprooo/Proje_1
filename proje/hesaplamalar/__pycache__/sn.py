def nmenu():
    a = int(input("1. sınav notunu gir"))
    b = int(input("1. performans notunu gir"))
    c = int(input("2. sınav notunu gir"))
    d = int(input("2. Performansnotunu gir"))
    e = (a+b+c+d)/4
    if e >=85 and e<=100 : print ("5 aldın")
    elif e >=70 and e<85 : print ("4 aldın")
    elif e >=50 and e<70 : print ("3 aldın")
    elif e >=35 and e<50 : print ("2 aldın")
    elif e >=20 and e< 35: print ("1 aldın")
    elif e == 0 : print ("0 aldın")    