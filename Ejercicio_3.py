#Crea una función llamada magia_numerica() que realice varias transformaciones en una lista de 
# números sin modificar la lista 

def magia_numerica(lista):
    # Paso 1: Eliminar elementos duplicados
    lista = list(set(lista))
    
    # Paso 2: Ordenar la lista de mayor a menor
    lista.sort(reverse=True)
    
    # Paso 3: Eliminar números impares
    lista = [i for i in lista if i % 2 == 0]
    
    # Paso 4: Sumar todos los números que quedan
    suma_total = sum(lista)
    
    # Paso 5: Colocar la suma como el primer elemento de la lista
    lista.insert(0, suma_total)
    
    #Comprueba  que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista.
    if lista[0]== sum(lista[1:]):
        mensaje = 'comprobacion correcta'
    else:
        mensaje ='comprobacion incorrecta'
        
    return lista,mensaje

#practica
nums = [5,4,3,0,9,2,7,1,3, 7, 9, 2, 4, 2, 6, 8, 8]
print(magia_numerica(nums))


