
import matplotlib.pyplot as plt
import numpy as np
import math
                                                                                                                                        
def grafica(x=[],y=[]):
    plt.plot(x,y,'r.')
    plt.show()


x1=float(input("Dijite x1->"))
y1=float(input("Dijite y1->"))
x2=float(input("Dijite x2->"))
y2=float(input("Dijite y2->"))

milistax=[]
milistay=[]
m=(y2-y1)/(x2-x1)
print(m)

if m<1:
    x1=x1+1.0
    yk=1.0
    for i in range(int(x1),int(x2+1)):
        yk=yk+m
        milistay.append(yk)
        milistax.append(i)
    print("Coordenadas en X ",milistax[:])  
    print("\n Coordenadas en Y ",milistay[:])
    grafica(milistax,milistay)
   

else:
    y1+1.0
    xk=1.0
    
    for i in range(int(y1),int(y2+1)):
        xk=xk+1/m
        milistax.append(xk)
        milistay.append(i)
      
    print("Coordenadas en x ",milistax[:])
    print("Coordenadas en y ",milistay[:])
    grafica(milistax,milistay)

  
    


 








