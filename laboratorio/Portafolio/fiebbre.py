while true:

try:
x=0
x=int(input("introduzca la temperatura:"))
except valueerror:
print("valor no valido")

if x> (37.5):
print (tienes fiebre")
if x< (30):
print ("estas enfermo")
if x ==0:
 breaj

elif x<(5):

def creartxt():
    archi=open('temp.dat','w')
    archi.close()

def grabartxt(a, b):
    archi=open('temp.dat','a')
    archi.write(a,b)

    archi.close()

def leertxt():
    print("ingresar datos")
    tem1=int(input("temperatura alta"))
    if tem1>37.5:
        print("tiene fiebre")
    elif tem1<37.5:
        print("esta enfermo")
    else:
        tem1<=5:
        print("esta enfermo")
    grabartxt(temp, b)


creartxt()
grabartxt()
leertxt()

