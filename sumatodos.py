def sumaTodos(limitTo):
    resultado=0
    for i in range(0, limitTo+1):
        resultado += i
    return resultado
    
print(sumaTodos(100))

# Funciones de primera clase
addAll = sumaTodos # Permiten asignarse a variables (entre otras opciones)

print(addAll(4))

# Función de nivel superior: Permite recibir funciones como parámetros o devolver una función
def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado =+ i*i
    return resultado
    
print(sumaTodosLosCuadrados(3))

