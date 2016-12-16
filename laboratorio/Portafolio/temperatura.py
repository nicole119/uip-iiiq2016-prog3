cont=0
control=0

def calcular(temp,cont) :

         if temp > 37.5:
            archivo = open('temp.txt','a')
            archivo.write(str(cont)+ ", "+str(temp)+ ", fiebre\n")
            archivo.close()
         if temp < 37.6 and temp > 30:
             archivo = open('temp.txt', 'a')
             archivo.write(str(cont) + ", "+str(temp) + ", normal\n")
             archivo.close()
         if temp < 5:
             archivo = open('temp.txt', 'a')
             archivo.write(str(cont) +", "+ str(temp) + ", muerto\n")
             archivo.close()
         if temp < 30 and temp > 5:
             archivo = open('temp.txt','a')
             archivo.write( str(cont)+", "+ str(temp)+  ", enfermo\n")
             archivo.close()


while control == 0:
    try:
        temp = float(input("digite temperatura: "))
        if temp == 0 :
            control=1
    except:
        print("invalido")


    else:
        cont+=1
        calcular (temp , cont)







