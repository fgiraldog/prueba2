# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo cruel")

def parabola(x):
        
            return x*x
       
    
x = np.linspace(0,1,100)

plt.figure()
plt.plot(x,parabola(x))
plt.show()