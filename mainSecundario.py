import numpy as np
#PASO 1: GENERAR NUMEROS RANDOM PARA CADA CROMOSOMA
# Número de cromosomas en la población
num_chromosomes = 6

# Define el rango de valores posibles para a, b, c y d (0-30 para cada uno)
min_value = 0
max_value = 30
# Generar los cromosomas con valores aleatorios para a, b, c y d
#population = np.random.randint(min_value, max_value + 1, size=(num_chromosomes, 4))

#AQUI VA LOS DATOS ESTSTICOS DE MI ALGORITMO GENETICO
population = np.array([[12,5,23,8],
               [2,21,18,3],
               [10,4,13,14],
               [20,1,10,6],
               [1,4,13,19],
               [20,5,17,1]])

# Imprimir la población inicial
for i, chromosome in enumerate(population, 1):
    print(f"Chromosome[{i}] = [a; b; c; d] = {list(chromosome)}")
    

#PASO 2: We compute the objective function value for each chromosome produced in initialization step
#f(x) = ((a + 2b + 3c + 4d) - 30)
def objectiveFunction(cromosoma):
    F_obj = np.zeros(cromosoma.shape[0])
   # F_obj = np.zeros(shape=5)
    F_obj[0] = abs((cromosoma[0,0] + (cromosoma[0,1] * 2) + (cromosoma[0,2] * 3) + (cromosoma[0,3] * 4)) - 30)
    F_obj[1] = abs((cromosoma[1,0] + (cromosoma[1,1] * 2) + (cromosoma[1,2] * 3) + (cromosoma[1,3] * 4)) - 30)
    F_obj[2] = abs((cromosoma[2,0] + (cromosoma[2,1] * 2) + (cromosoma[2,2] * 3) + (cromosoma[2,3] * 4)) - 30)
    F_obj[3] = abs((cromosoma[3,0] + (cromosoma[3,1] * 2) + (cromosoma[3,2] * 3) + (cromosoma[3,3] * 4)) - 30)
    F_obj[4] = abs((cromosoma[4,0] + (cromosoma[4,1] * 2) + (cromosoma[4,2] * 3) + (cromosoma[4,3] * 4)) - 30)
    F_obj[5] = abs((cromosoma[5,0] + (cromosoma[5,1] * 2) + (cromosoma[5,2] * 3) + (cromosoma[5,3] * 4)) - 30)
    return F_obj

f_result = objectiveFunction(population)
print(f_result.shape)    
print("f(x) = "+ str(f_result))

#PASO 3: FUNCION FITNESS
def fitnessFunction(functionResult):
    #Fitness[1] = 1 / (1+F_obj[1])
    Fitness = np.zeros(functionResult.shape)
    Fitness[0] = 1 / (1+functionResult[0])
    Fitness[1] = 1 / (1+functionResult[1])
    Fitness[2] = 1 / (1+functionResult[2])
    Fitness[3] = 1 / (1+functionResult[3])
    Fitness[4] = 1 / (1+functionResult[4])
    Fitness[5] = 1 / (1+functionResult[5])
    
    total = Fitness[0]+Fitness[1]+Fitness[2]+Fitness[3]+Fitness[4]+Fitness[5]
    return Fitness, total
fitnessResult = fitnessFunction(f_result)
print("fitness = "+str(fitnessResult[0]))    
print("total = "+ str(fitnessResult[1]))

def probabilityFunction(fitnessResult):
    #P[i] = Fitness[i] / Total
    fitness = fitnessResult[0]
    total = fitnessResult[1]
    P = np.zeros(fitness.shape)
    P[0] = fitness[0] / total
    P[1] = fitness[1] / total
    P[2] = fitness[2] / total
    P[3] = fitness[3] / total
    P[4] = fitness[4] / total
    P[5] = fitness[5] / total
    return P

probabilityResult = probabilityFunction(fitnessResult)    
print("P = "+ str(probabilityResult))

def probabilityComulative(pResult):
     p = pResult
    #C[i] = 0.1254 + n
     C = np.zeros(probabilityResult.shape)
     C[0] = p[0]
     C[1] = p[0] + p[1]
     C[2] = p[0] + p[1] + p[2]
     C[3] = p[0] + p[1] + p[2] + p[3]
     C[4] = p[0] + p[1] + p[2] + p[3] + p[4]
     C[5] = p[0] + p[1] + p[2] + p[3] + p[4] + p[5]
     return C
     
comulativeResult = probabilityComulative(probabilityResult)    
print("C = "+ str(comulativeResult))

##ESTE ES MI ARREGLO DE RANDOMS LO COMENTO PARA HACERLO COMO LA TABLA
#nRandom = np.random.rand(6)
nRandom = np.array([[0.201],[0.284],[0.099],[0.822],[0.398],[0.501]])
print("nRandom = "+ str(nRandom))

probCom = comulativeResult


NewChromosome = np.zeros(population.shape)

#for i in range(0, 6):
for i in range(len(population)):

    if nRandom[i] > probCom[0] and nRandom[i] < probCom[1]:
        NewChromosome[i] = population[1]
        print(f"NewChromosome[{i}] PosA[{2}] = [a; b; c; d] = {NewChromosome[i]}")
        
    elif nRandom[i] > probCom[1] and nRandom[i] < probCom[2]:
        NewChromosome[i] = population[2]
        print(f"NewChromosome[{i}] PosA[{3}] = [a; b; c; d] = {NewChromosome[i]}")
        
    elif nRandom[i] > probCom[2] and nRandom[i] < probCom[3]:
        NewChromosome[i] = population[3]
        print(f"NewChromosome[{i}] PosA[{4}] = [a; b; c; d] = {NewChromosome[i]}")
        
    elif nRandom[i] > probCom[3] and nRandom[i] < probCom[4]:
        NewChromosome[i] = population[4]
        print(f"NewChromosome[{i}] PosA[{5}] = [a; b; c; d] = {NewChromosome[i]}")
        
    elif nRandom[i] > probCom[4] and nRandom[i] < probCom[5]:
        NewChromosome[i] = population[5]
        print(f"NewChromosome[{i}] PosA[{6}] = [a; b; c; d] = {NewChromosome[i]}")
        
    elif nRandom[i] < probCom[0]:
        NewChromosome[i] = population[0]
        print(f"NewChromosome[{i}] PosA[{1}] = [a; b; c; d] = {NewChromosome[i]}")
        
# Convertir NewChromosome al tipo de datos de population
NewChromosome = NewChromosome.astype(population.dtype)

np.copyto(population, NewChromosome)
#print(f"NewChromosome[{i}] = [a; b; c; d] = {NewChromosome[i]}")

#EN ESTE PUNTO AHORA SIGUE LO DE SELECCIONAR NUEVOS RANDOMS PARA SACAR LA NUEVA GENERACION
pc = .25
k = 0
i = 0
#R = np.zeros(population.shape)
R = np.array([[0.191],[0.259],[0.760],[0.006],[0.159],[0.340]])
parentPos = np.empty(3)
while k < len(population):
    #este lo activo cuando ya los reemplzae con random
   # R[k] = np.random.rand
    if R[k] < pc:
       parentPos[i] = k
       #AQUI GUARDO EN PARENT POSITION K QUE ES LA POSICION DEL CROMOSOMA QUE FUE MENOR DE .25(PC)
       # parent[k] = k
       i = i + 1# LE VOY AUMENTANDO AL INDICE SI EL IF HIZO MATCH, PARA SEGUIR GUARDANDO EN PARENT
    
    k = k + 1

#MOSTRAR NUEVOS RANDOM
print("Random2 = "+ str(R))

#MOSTRAR LA SELECCION DE CROSSOVER PARA LO DE LA PROBABILIDAD MENOR A .25%
print("Posiciones de cromosomas para crossover menor a 25% = "+ str(parentPos))
#APARTIR DE AQUI SELECCIONAREMOS CUAL ES EL PUNTO DE CRUZE ENTRE LAS POSICIONES
#crossPoint = np.empty(parentPos.astype(int))
crossPoint = np.empty(3)
for i in range(len(parentPos)):
    # se genera de 1 a cromosomas -1 que seria abcd son 4 -1 son 3
    crossPoint[i] = np.random.randint(1, population.shape[1] - 1)
    
cp = crossPoint
print("Los puntos de cruze son " + str(cp))
        
    #recibe dos parametros la posicion de los cromosomas seleccionados y los puntos de cruze
    #tambien se requeriran los cromosomas
def crossoverPoints(pos,point, cromosoma):
    pointC1 = point[0]
    pointC2 = point[1]
    pointC3 = point[2]
   # NewChromosome = NewChromosome.astype(population.dtype) esto es solo de ejemplo
   # pos = pos.astype(cromosoma.dtype) #Este si funciona
    cromosoma = cromosoma.astype(int)
    pos = pos.astype(int)
    # Crear una copia temporal del arreglo porque si guardo en el principal los siguientes cruces tomaran los nuevos datos envez de los anteriores
    temp = np.copy(cromosoma)
    #lo qu hago es que para cada cromosoma que tomo de point(posiciones de cromosomas) le extraigo
    #cada gen que seria abcd, son diferentes ifs, en caso de que el punto de cruce sea 1
    #pues solo tomara 1 y los otros 3 del otro array, si son 2 pues toma 2 del primero y 2 del otro, 
    #y si sonn 3 pues toma 3 del primero y 1 del otro, PARA ESO SIRVEN LOS IFS(NOTA PERSONAL TRATAR DE IMPLEMENTARLO CON UN FOR PARA AHORRAR CODIGO)
    #primer cruce  Chromosome[1] >< Chromosome[4]
    gen1 = cromosoma.item(pos[0],0)
    if pointC1 == 1:
        gen2 = cromosoma.item(pos[0+1],1)
        gen3 = cromosoma.item(pos[0+1],2)
        gen4 = cromosoma.item(pos[0+1],3)
    elif pointC1 == 2:
        gen2 = cromosoma.item(pos[0],1)
        gen3 = cromosoma.item(pos[0+1],2)
        gen4 = cromosoma.item(pos[0+1],3)
    elif pointC1 == 3:
        gen2 = cromosoma.item(pos[0],1)
        gen3 = cromosoma.item(pos[0],2)
        gen4 = cromosoma.item(pos[0+1],3)
    
    temp[pos[0]] = [gen1, gen2, gen3, gen4]
    #cromosoma[pos[0]] = [gen1,gen2,gen3,gen4]
    #segundo cruce Chromosome[4] >< Chromosome[5]
    gen1 = cromosoma.item(pos[1],0)
    if pointC2 == 1:
        gen2 = cromosoma.item(pos[1+1],1)
        gen3 = cromosoma.item(pos[1+1],2)
        gen4 = cromosoma.item(pos[1+1],3)
    elif pointC2 == 2:
        gen2 = cromosoma.item(pos[1],1)
        gen3 = cromosoma.item(pos[1+1],2)
        gen4 = cromosoma.item(pos[1+1],3)
    elif pointC2 == 3:
        gen2 = cromosoma.item(pos[1],1)
        gen3 = cromosoma.item(pos[1],2)
        gen4 = cromosoma.item(pos[1+1],3)
        
    temp[pos[1]] = [gen1, gen2, gen3, gen4]
    #cromosoma[pos[1]] = [gen1,gen2,gen3,gen4]
    
    #tecer cruce Chromosome[5] >< Chromosome[1]
    gen1 = cromosoma.item(pos[2],0)
    if pointC3 == 1:
        gen2 = cromosoma.item(pos[0],1)
        gen3 = cromosoma.item(pos[0],2)
        gen4 = cromosoma.item(pos[0],3)
    elif pointC3 == 2:
        gen2 = cromosoma.item(pos[2],1)
        gen3 = cromosoma.item(pos[0],2)
        gen4 = cromosoma.item(pos[0],3)
    elif pointC3 == 3:
        gen2 = cromosoma.item(pos[2],1)
        gen3 = cromosoma.item(pos[2],2)
        gen4 = cromosoma.item(pos[0],3)
    
    #cromosoma[pos[2]] = [gen1,gen2,gen3,gen4]
    temp[pos[2]] = [gen1, gen2, gen3, gen4]
    
    #MUEVO MI ARREGLO COPIA AL PRINCIPAL PARA REFLEJAR LOS CAMBIOS
    cromosoma = temp
    return cromosoma

NewChromosome2 = crossoverPoints(parentPos,cp,population)
np.copyto(population, NewChromosome2)
print("Matriz con cruces \n" + str(population))
       
    
    
#AQUI COMIENZA LO DE LA MUTACION
#total_gen = number_of_gen_in_Chromosome * number of population
total_gen = 4 * 6           
    
#Mutation process is done by generating a random integer between 1 and total_gen (1 to 24). 24 total de genes del cromosoma
#Suppose we define ρm 10%, it is expected that 10% (0.1) of total_gen in the population that will be mutated
number_of_mutations = 0.1 * 24
    
#The value of mutated gens at mutation point is replaced by random number between 0-30.

def mutationPoints(total_gen,number_of_mutations,cromosomas):
    #para poder iterar en number_of lo converitmos a int para que redonde el numero de mutaciones
    number_of_mutations = int(number_of_mutations)
    print("numero de mutaciones " + str(number_of_mutations))
    arrPosition = np.array([])
    arrCambios = np.array([])
    
    for i in range(number_of_mutations):
        #Este random es la posicion de lappoblacion que se reemplazara
        Rposition = np.random.randint(1,total_gen + 1)
        arrPosition = np.append(arrPosition, Rposition)
        
        #Este random es el numero por el cual se reemplazara 1 - 30
        Rcambio = np.random.randint(1,31)
        arrCambios = np.append(arrCambios, Rcambio)
        
        #AQUI HAGOEL INTERCAMBIO EN LA POSICION SELECCIONADA
        #np.place(cromosomas, cromosomas == Rposition -1, Rcambio)
        #PLACE NO ME FUNCIONO HAY QUE USAR PUT PORQUE SE ESPECIFICA LA POSICION SIN SABER EL IDNICE
        np.put(cromosomas,Rposition-1, Rcambio)
    return cromosomas, arrPosition, arrCambios
    
mutationResults = mutationPoints(total_gen,number_of_mutations, population)
print("posicion seleccionada" + str(mutationResults[1]))
print("numero de reemplazo" + str(mutationResults[2]))
np.copyto(population, mutationResults[0])
print("CROMOSOMAS MUTADOS \n" + str(population) )
f_result2 = objectiveFunction(population)
print("Nueva f(x) = "+ str(f_result2))
        
        
    
    