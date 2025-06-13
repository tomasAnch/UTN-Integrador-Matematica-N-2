# --- PARTE A: OPERACIONES CON DNIs ---

def ingresar_dnis(num_integrantes):
    dnis = []         # Lista para guardar los DNIs ingresados
    conjuntos = []    # Lista para guardar los conjuntos de dígitos únicos

    # Repetimos la cantidad de veces que hay integrantes
    for i in range(num_integrantes):
        dni = input(f"Ingrese el DNI del integrante {i+1} : ")
        dnis.append(dni)

        # Creamos una lista para guardar los dígitos como números
        digitos = []
        for d in dni:
            numero = int(d)
            digitos.append(numero)

        # Convertimos la lista en un conjunto para eliminar repetidos
        conjunto = set(digitos)

        # Agregamos el conjunto a la lista de conjuntos
        conjuntos.append(conjunto)

    # Devolvemos las dos listas: los DNIs originales y sus conjuntos de dígitos únicos
    return dnis, conjuntos

# Función para contar frecuencia de dígitos en un DNI usando ciclo for
def contar_frecuencia(dni):
    frecuencia = {} #diccionario vacio que va a guardar cuantas veces aparece el digito.
    for digito in dni:
        if digito in frecuencia:
            frecuencia[digito] += 1 #Si el dígito ya está en el diccionario, le sumamos 1 al contador.
        else:
            frecuencia[digito] = 1 #Si no está, significa que es la primera vez que lo vemos, entonces lo agregamos al diccionario con valor 1.
    return frecuencia

# Función para sumar todos los dígitos de un DNI
def sumar_digitos(dni):
    total = 0
    for digito in dni:
        total += int(digito)
    return total

# --- PROGRAMA PRINCIPAL PARTE A ---

def main_parte_A():
    print("Trabajo Integrador: Matemáticas y Python - PARTE A\n")

    integrantes = 3

    dnis, conjuntos = ingresar_dnis(integrantes)

    print("\nConjuntos de dígitos únicos por cada DNI:")
    for i, conjunto in enumerate(conjuntos):
        print(f"Integrante {i+1}: {conjunto}")

    A, B, C = conjuntos[0], conjuntos[1], conjuntos[2]

    print("\nOperaciones entre conjuntos:\n")

    # UNIONES - Junta todos los elementos sin repetir
    print("UNIÓN:")
    print("A ∪ B:", A.union(B))
    print("A ∪ C:", A.union(C))
    print("B ∪ C:", B.union(C))
    print()

    # INTERSECCIONES - Busca los elementos comunes
    print("INTERSECCIÓN:")
    print("A ∩ B:", A.intersection(B))
    print("A ∩ C:", A.intersection(C))
    print("B ∩ C:", B.intersection(C))
    print()

    # DIFERENCIAS - Muestra lo que hay en uno pero no en el otro
    print("DIFERENCIA:")
    print("A - B:", A.difference(B))
    print("B - A:", B.difference(A))
    print("A - C:", A.difference(C))
    print("C - A:", C.difference(A))
    print("B - C:", B.difference(C))
    print("C - B:", C.difference(B))
    print()

    # DIFERENCIA SIMÉTRICA - Muestra lo que hay en uno o en otro, pero no en los dos
    print("DIFERENCIA SIMÉTRICA:")
    print("A Δ B:", A.symmetric_difference(B))
    print("A Δ C:", A.symmetric_difference(C))
    print("B Δ C:", B.symmetric_difference(C))
    print()

    # Frecuencia y suma de dígitos por DNI
    print("FRECUENCIA Y SUMA DE DÍGITOS:")
    for i, dni in enumerate(dnis):
        cantidad_por_digito = contar_frecuencia(dni)
        suma_total = sumar_digitos(dni)
        print(f"Integrante {i+1} - DNI: {dni}")
        print(f"Cantidad de cada dígito: {cantidad_por_digito}")
        print(f"Suma total de dígitos: {suma_total}")
        print()

    # Condición 1: alta diversidad numérica
    if len(A) >= 5 and len(B) >= 5 and len(C) >= 5:
        print("Hay alta diversidad numérica.")
    else:
        print("No se cumple la condición de alta diversidad numérica.")

    # Condición 2: dígito común en todos los conjuntos
    comunes = A.intersection(B).intersection(C)
    if comunes:
        print(f"Dígitos comúnes en todos los conjuntos: {comunes}")
    else:
        print("No hay ningún dígito común en todos los conjuntos.")

# --- PARTE B: OPERACIONES CON AÑOS DE NACIMIENTO ---

def ingresar_anos(num_integrantes):
    anos = []  # Creamos una lista vacía para guardar los años de nacimiento
    for i in range(num_integrantes):
        # Pedimos que el usuario ingrese el año de nacimiento de cada integrante
        ano = int(input(f"Ingrese el año de nacimiento del integrante {i+1}: "))
        anos.append(ano)  # Agregamos el año ingresado a la lista
    return anos  # Devolvemos la lista completa con todos los años

def es_bisiesto(ano):
    # Función que recibe un año y devuelve True si es bisiesto, False si no lo es
    # Un año es bisiesto si:
    #  - Es divisible por 400, o
    #  - Es divisible por 4 pero no por 100
    if ano % 400 == 0:
        return True
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    return False  # Si no cumple ninguna condición, no es bisiesto

def contar_pares_impares(anos):
    pares = 0  # Inicializamos contador de años pares
    impares = 0  # Inicializamos contador de años impares
    for ano in anos:  # Recorremos cada año en la lista
        if ano % 2 == 0:  # Si el año es divisible por 2, es par
            pares += 1    # Sumamos 1 al contador de pares
        else:
            impares += 1  # Si no, sumamos 1 al contador de impares
    return pares, impares  # Devolvemos ambos contadores

def producto_cartesiano(conjunto1, conjunto2):
    resultado = []  # Lista vacía para guardar el resultado
    for elem1 in conjunto1:  # Recorremos cada elemento del primer conjunto
        for elem2 in conjunto2:  # Por cada elemento del segundo conjunto
            resultado.append((elem1, elem2))  # Agregamos la pareja (elem1, elem2) a la lista
    return resultado  # Devolvemos la lista con todas las parejas

# --- PROGRAMA PRINCIPAL PARTE B ---

def main_parte_B():
    print("\nTrabajo Integrador: Matemáticas y Python - PARTE B\n")

    integrantes = 3  # Definimos la cantidad de integrantes

    # Llamamos a la función para ingresar años y guardamos la lista resultante
    anos = ingresar_anos(integrantes)

    # Contamos cuántos años son pares y cuántos impares usando la función creada
    pares, impares = contar_pares_impares(anos)
    print(f"\nCantidad de integrantes que nacieron en años pares: {pares}")
    print(f"Cantidad de integrantes que nacieron en años impares: {impares}")

    # Verificamos si todos los años son mayores a 2000
    todos_despues_2000 = True  # Suponemos que sí, hasta que encontremos uno que no
    for ano in anos:
        if ano <= 2000:
            todos_despues_2000 = False  # Cambiamos a falso si encontramos un año menor o igual a 2000
            break  # No hace falta seguir revisando, salimos del ciclo

    if todos_despues_2000:
        print("Grupo Z")  # Si todos nacieron después del 2000, mostramos este mensaje

    # Verificamos si alguno nació en un año bisiesto
    alguno_bisiesto = False  # Suponemos que no, hasta que encontremos uno que sí
    for ano in anos:
        if es_bisiesto(ano):  # Usamos la función que definimos para saber si es bisiesto
            alguno_bisiesto = True
            break  # Si encontramos uno, salimos del ciclo

    if alguno_bisiesto:
        print("Tenemos un año especial (bisiesto).")  # Mostramos mensaje si hay algún año bisiesto

    # Para hacer el producto cartesiano necesitamos dos conjuntos:
    # Aquí suponemos un conjunto fijo de edades actuales para los integrantes
    edades = [20, 22, 24]

    # Calculamos el producto cartesiano entre años y edades
    producto = producto_cartesiano(set(anos), set(edades))
    print("\nProducto cartesiano entre años de nacimiento y edades actuales:")
    for par in producto:  # Mostramos cada pareja del producto cartesiano
        print(par)  

if __name__ == "__main__":
    main_parte_A()
    main_parte_B()


