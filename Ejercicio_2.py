
texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

#cambiamos los # por saltos de linea
texto_formateado = texto_original.replace('#','\n')

#Creamos una lista y añadimos un punto al final de cada linea
lineas = texto_formateado.split("\n")
lineas =  [linea+'.' for linea in lineas]
#La primera en mayuscula
lineas = [linea.capitalize() for linea in lineas]

#Añadimos los ptos supensivos a la rpimera linea 
print(lineas[0]+'..')

#Hacemos los saltos de lineas y la tabulacion con un bucle a partir de la segunda linea 
for linea in lineas[1:]:
    print(f'\t·{linea}')
final = "\n".join(lineas)