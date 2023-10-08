#Construye tu Propio Universo Estelar
import math
#1 Crea una clase llamada Estrella con tres coordenadas
class Estrella:
    
#2 Añade un método constructor para generar estrellas fácilmente. Si no se reciben coordenadas, las coordenadas por defecto serán cero.
    def __init__(self,nombre,x=0,y=0,z=0):
        self.nombre= nombre
        self.x=x
        self.y=y
        self.z=z
        
#3 Implementa el método __str__ para que al imprimir la estrella, las coordenadas aparezcan en el formato .
    def __str__(self):
        return 'La estrella {} tiene coordenadas: x={} y={} z={}'.format(self.nombre,self.x,self.y,self.z)
    
#4 Agrega un método galaxia para determinar en qué galaxia del universo podría estar ubicada la estrella basada en sus coordenadas.
    def galaxia(self):
        if self.x <0:
            return "Galaxia Magallanes"
        elif self.y <0:
            return "Galaxia Sagitario"
        elif self.z <0:
            return "Galaxia Via Lactea"
        else:
            return "Galaxia no conocida"
        
#5 Implementa un método distancia para calcular la distancia entre dos estrellas usando la fórmula de distancia en el espacio 3D.
    def distancia(self, otra):
        d_x= self.x-otra.x
        d_y= self.y-otra.y
        d_z= self.x-otra.z
        distancia = math.sqrt(d_x**2+d_y**2+d_z**2)
        return distancia 
#Experimento
A = Estrella('A',2,3,1)
B = Estrella('B',4,4,4)
C= Estrella('C',-3,-1,0)
O = Estrella('O',0,0,0)

print(A.__str__())
print(B.__str__())
print(C.__str__())

print(A.galaxia())
print(B.galaxia())
print(C.galaxia())

print('La distancia de A con B es',A.distancia(B))
print('La distancia de B con C es',B.distancia(C))


d_A = A.distancia(O)
d_B= B.distancia(O)
d_C= C.distancia(O)
print('La distancia de A con el origen es:', d_A)
print('La distancia de B con el origen es:', d_B)
print('La distancia de C con el origen es:', d_C)


        