def hmmenu ():
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                                                                            ║")
    print("║                                                        Hesap Makinesi                                                      ║")
    print("║                                                                                                                            ║")
    print("║             Toplama = 1                                                                                                    ║")
    print("║                                                                                                                            ║")
    print("║                                                                                                                            ║")
    print("║             Çarpma = 2                                                                                                     ║")
    print("║                                                                                                                            ║")
    print("║                                                                                                                            ║")
    print("║             Çıkarma = 3                                                                                                    ║")
    print("║                                                                                                                            ║")
    print("║                                                                                                                            ║")
    print("║             Bölme = 4                                                                                                      ║")
    print("║                                                                                                                            ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    ha = float(input(" methodu gir "))
    hb = float(input(" 1. sayıyı gir "))
    hc = float(input("2. sayıyı gir "))
    if   ha==1 : print (hb+hc)
    elif ha==2 : print (hb*hc)
    elif ha==3 : print (hb-hc)
    elif ha==4 : print (hb/hc)
    
    else: print ("yanlış method")
    input()