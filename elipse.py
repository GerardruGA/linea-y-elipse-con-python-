import matplotlib.pyplot as plt
import numpy as np
import math

def grafica(x=[],y=[]):
    plt.plot(x,y,'r.')
    plt.show()


r=float(input("Dijite r->"))
R=float(input("Dijite R->"))
conteo=int(input("Dijite el conteo en grados ->"))

vecx=[]
vecy=[]

for i in range(0,360,conteo):

    conteo2=float(i)
    x = math.radians(conteo2)
    x=math.cos(x)
    puntox=float((r)*(x))
    vecx.append(puntox)
   


for i in range(0,360,conteo):
    conteo3=float(i)
    x=math.radians(conteo3)
    x=math.sin(x)
    puntoy=((R)*(x))
    vecy.append(puntoy)

grafica(vecx,vecy)

#Una vez calculado el centro como si fuera el origen se procede a agregar los  datos del siguiente punto

nuevo_puntox=float(input("Dijite un nuevo punto en x-> "))
nuevo_puntoy=float(input("Dijite el nuevo punto en y->"))

longitud_vect=len(vecx)
for i in range(longitud_vect):
   vecx[i]=vecx[i]+nuevo_puntox
   vecy[i]=vecy[i]+nuevo_puntoy

grafica(vecx,vecy)

     


    
    


