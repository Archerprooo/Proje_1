import random
import datetime
import turtle
hak = int(input("hak sayını gir : "))
son = int(input("son sınırı gir : "))
bas = int(input("ilk sınırı gir : "))
puan = 100
tutulan = random.randint(bas,son)

print (f"ben {bas} ile {son} arası bir sayı tuttum")
print (f"{hak} hakkın var")
for xx in range(hak):
    tahmin = int (input("tahminin nedir"))
    if tahmin > son or tahmin < bas : print (f"{bas} ile {son} arası sayı tut ceza olarak 1 hakkın gitti")
    if tahmin == tutulan:
        print("bildin")
        print (puan)
        break
    elif tahmin  > tutulan :
        print ("tahminin büyük")
        puan -= 100//hak
        print (f"puann{puan} oldu")
    elif tahmin  < tutulan :
        print ("tahminin küçük") 
        puan -= 100//hak
        print (f"puann{puan} oldu")
    if xx == hak :
        print (f"bilemedin sayı {tutulan}dı") 
    