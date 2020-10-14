#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
def get_xy_arrays(degree, coefficients, x_start, x_end):
    x = np.linspace(x_start,x_end,100)
    if degree == 4:
        f_x = (coefficients[0]*x**degree + coefficients[1]*x**(degree-1) + coefficients[2]*x**(degree-2) + coefficients[3]*x**(degree-3) + coefficients[4]*x**(degree-4))
    if degree == 3:
        f_x = (coefficients[0]*x**degree + coefficients[1]*x**(degree-1) + coefficients[2]*x**(degree-2) + coefficients[3]*x**(degree-3))
    if degree == 2:
        f_x = (coefficients[0]*x**degree + coefficients[1]*x**(degree-1) + coefficients[2]*x**(degree-2))
      
    """
    Genera los arreglos de x y f(x) para representar la función.

    Entradas:
     - degree (int): el grado del polinomio, solo puede ser 2, 3 o 4
     - coefficients (list): Una lista con los coeficientes, empezando con
       el coeficiente para la x con mayor exponente
     - x_start (int/float): El inicio del intervalo en x
     - x_end (int/float): El final del intervalo en x
    Salidas:
     - x (np.array): arreglo con los valores del intervalo de x
     - f_x (np.array): arreglo con los valores de f(x)
    """

    return x, f_x
#%%
def find_cp(x, f_x):
    
    """
    Encuentra los índices de f_x donde se encontraron puntos críticos y los tipos de puntos críticos

    Entrada:
     - x (np.array): arreglo con los valores del intervalo de x.
     - f_x (np.array): arreglo de los valores de f(x) para la función a evaluar.

    Salida:
     - indxs (list/np.array()): Los índices de f_x donde hay puntos críticos.
     - types (list): Lista que define si el punto crítico es un mínimo ('min') o un máximo ('max'). 
       Ej. Para una función con dos puntos críticos, si el primero es un mínimo
       y el segundo un máximo, se debe regresar la lista, ['min','max'].
    """
    # Como necesitamos empezar con una pendiente anterior antes de hacer tu ciclo encuentra
    # la pendiente entre los dos primeros valores

    last_slope = (f_x[1]-f_x[0])/(x[1]-x[0])

    # Crea las listas a regresar

    indxs = []
    types = []

    # Queremos hacer un ciclo para calcular cada pendiente, como ya calculamos la pendiente entre
    # el primer y segundo punto, empezamos con el índice 2.

    for i in range(2,len(f_x)):
        # Calcula la nueva pendiente
        this_slope = (f_x[i]-f_x[i-1])/(x[i]-x[i-1])
        
        if (this_slope*last_slope) <= 0:
            indxs.append(i)
            if last_slope < 0:
                types.append('min')
            elif last_slope > 0:
                types.append('max')
        else:
            continue

        last_slope = this_slope
        
    return indxs, types
#%%


#%%

