from GeneticAlgorithm import AlgoritmoGenetico
import numpy as np

#PASO 1: GENERAR NUMEROS RANDOM PARA CADA CROMOSOMA
# Número de cromosomas en la población
num_chromosomes = 6
# Define el rango de valores posibles para a, b, c y d (0-30 para cada uno)
min_value = 0
max_value = 30
# Generar los cromosomas con valores aleatorios para a, b, c y d
population = np.random.randint(min_value, max_value + 1, size=(num_chromosomes, 4))

#AQUI VA LOS DATOS ESTSTICOS DE MI ALGORITMO GENETICO
#population = np.array([[12,5,23,8],
 #              [2,21,18,3],
  #             [10,4,13,14],
   #            [20,1,10,6],
    #           [1,4,13,19],
     #          [20,5,17,1]])

# Imprimir la población inicial
for i, chromosome in enumerate(population, 1):
    print(f"Chromosoma[{i}] = {list(chromosome)}")
#----------------------declaro mi objeto------------------------------
ag = AlgoritmoGenetico(population)
#------funcion----------------------------------------------------
generations = 0
while True:
    print("f(x) = "+ str(ag.objectiveFunction()))
    #AQUI LE INDICO QUE SI ENCEUNTRA UNA QUE SEA IGUAL A 30 SE DETENGA
    if any(ag.objectiveFunction() == 30):
        print("Se encontró una solución satisfactoria en la generación", generations)
    #Y SI NO SE ENCONTRO EN 50 GENERACIONES QUE SALGA
    elif generations >= 4400:
        print("No se encontró una solución satisfactoria después de 50 generaciones")
        break

    #AQUI VA EL FITNESS Y LO DEL TOTAL
    print("fitness = "+str(ag.fitnessFunction()[0]))    
    print("total = "+ str(ag.fitnessFunction()[1]))
    print("-----------------------------------------------")
    #CODIGO DE LA PROBABILIDAD del resultado
    print("P = "+ str(ag.probabilityFunction()))

    #PROBABILIDAD COMULATIVA
    print("C = "+ str(ag.probabilityComulative()))

    #Comparaciones random
    print("Comparacion del if lo puse antes porque el print lo puse aqui envez de haya \n"+ str(ag.comparacionesRandom()))
    #NUMEROS RANDOM
    print("R = "+ str(ag.nRandom))

    ag.seleccionar_padres()
    print("R2 = "+ str(ag.nRandom))
    print("-----------------------------------------------")


    #ag.crossoverPoints()
    print("-----------------------------------------------")
    print("Matriz con cruces \n" + str(ag.crossoverPoints()))
    print("Posiciones cromosomas menor a 25% = "+ str(ag.parentPos))
    print("Los puntos de cruze son " + str(ag.crossPoint))
    print("-----------------------------------------------")

    mutation_points = ag.mutationPoints()
    print("NUMERO DE MUTACIONES " + str(mutation_points[3]))
    print("posicion seleccionada " + str(mutation_points[1]))
    print("numero de reemplazo" + str(mutation_points[2]))
    print("CROMOSOMAS MUTADOS \n" + str(mutation_points[0]) )
    
    generations += 1


