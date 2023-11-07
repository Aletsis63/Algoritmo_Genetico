#ALGORITMO GENETICO EN PYTHON
import numpy as np
class AlgoritmoGenetico:
    def __init__(self, poblacion_inicial):
        self.cromosomas = poblacion_inicial
        self.parentPos = np.empty(0)
        #el crosspoint debe de ser de los genes de cromosoma -1 osea abcd 4 - 3, lo dejare estatico pero puedo cambiarlo luego para el proeycto 
       # self.crossPoint = np.empty(3)#esto es lo que tendre que modificar para que sea co todos los que hicieron match en el if y no solo 3
        self.nRandom = np.array([])

    #PASO 2: We compute the objective function value for each chromosome produced in initialization step
    #f(x) = ((a + 2b + 3c + 4d) - 30)
    def objectiveFunction(self):
        F_obj = np.zeros(self.cromosomas.shape[0])
        for i in range(self.cromosomas.shape[0]):
            F_obj[i] = abs((self.cromosomas[i,0] + (self.cromosomas[i,1] * 2) + (self.cromosomas[i,2] * 3) + (self.cromosomas[i,3] * 4)) - 30)
        return F_obj
        
    #PASO 3: FUNCION FITNESS
    def fitnessFunction(self):
        #Fitness[1] = 1 / (1+F_obj[1]) EJEMPLO
        functionResult = self.objectiveFunction()
        Fitness = np.zeros(functionResult.shape)
        total = 0
        
        for i in range(self.cromosomas.shape[0]):
            Fitness[i] = 1 / (1+functionResult[i])
            total += Fitness[i]
                        
        return Fitness, total
    

    def probabilityFunction(self):
        #P[i] = Fitness[i] / Total EJEMPLO
        #fitnessResult = self.fitnessFunction
        fitness = self.fitnessFunction()[0]
        total = self.fitnessFunction()[1]
        P = np.zeros(fitness.shape)
        for i in range(self.cromosomas.shape[0]):
             P[i] = fitness[i] / total
        return P

    def probabilityComulative(self):
        p = self.probabilityFunction()
        #C[i] = 0.1254 + n
        C = np.zeros(p.shape)
        C[0] = p[0]
        for i in range(self.cromosomas.shape[0]):
            C[i] = p[i]
            C[i] = C[i-1] + p[i]
        
        return C
     

    def comparacionesRandom(self):
        NewChromosome = np.zeros(self.cromosomas.shape)
        self.nRandom = np.random.rand(self.cromosomas.shape[0])
        #self.nRandom = np.array([[0.201],[0.284],[0.099],[0.822],[0.398],[0.501]])

        #for i in range(0, 6):
        for i in range(len(self.cromosomas)):
            
            for j in range(len(self.probabilityComulative()) - 1):
             if self.nRandom[i] > self.probabilityComulative()[j] and self.nRandom[i] < self.probabilityComulative()[j+1]:
                NewChromosome[i] = self.cromosomas[j+1]
                print(f"NewChromosome[{i}] PosA[{j+2}] = [a; b; c; d] = {NewChromosome[i]}")
                
            if self.nRandom[i] < self.probabilityComulative()[0]:
                NewChromosome[i] = self.cromosomas[0]
                print(f"NewChromosome[{i}] PosA[{1}] = [a; b; c; d] = {NewChromosome[i]}")
           
        # Convertir NewChromosome al tipo de datos de self.cromosomas
        NewChromosome = NewChromosome.astype(self.cromosomas.dtype)

        #guardar los nuevos cambios de los nuevos cromosomas a la poblacion inicial
        np.copyto(self.cromosomas, NewChromosome)
        #return self.cromosomas
        #print(f"NewChromosome[{i}] = [a; b; c; d] = {NewChromosome[i]}")
        
        
        
    #EN ESTE PUNTO AHORA SIGUE LO DE SELECCIONAR NUEVOS RANDOMS PARA SACAR LA NUEVA GENERACION
    def seleccionar_padres(self):

        pc = .30
        k = 0
        i = 0
        #self.nRandom = np.zeros(self.cromosomas.shape)
       # self.nRandom = np.array([[0.191],[0.259],[0.760],[0.006],[0.159],[0.300]]) #ESTO LO VOY A TENER QUE CAMBIAR PARA LAS SIGUIENTES POR VALORES RANDOM EL PROBELMA ES LO DE HACER EL SWITCH O EL FOR QUE ESTA DIFICIL
        self.nRandom = np.random.rand(len(self.cromosomas))
        
        tam = 0
        for j in range(len(self.nRandom)):
             if self.nRandom[j] <= pc:
                tam += 1
            
        self.parentPos = np.empty(tam)
        
        #self.nRandom = np.random.rand(6)
        while k < len(self.cromosomas):
            #este lo activo cuando ya los reemplzae con random
        # self.nRandom[k] = np.random.rand
          if self.nRandom[k] <= pc:
            self.parentPos[i] = k
            #AQUI GUARDO EN PARENT POSITION K QUE ES LA POSICION DEL CROMOSOMA QUE FUE MENOR DE .25(PC)
            # parent[k] = k
            i = i + 1# LE VOY AUMENTANDO AL INDICE SI EL IF HIZO MATCH, PARA SEGUIR GUARDANDO EN PARENT
            
          k = k + 1

        #APARTIR DE AQUI SELECCIONAREMOS CUAL ES EL PUNTO DE CRUZE ENTRE LAS POSICIONES
        #crossPoint = np.empty(self.parentPos.astype(int))
        self.crossPoint = np.empty(len(self.parentPos))
        for i in range(len(self.parentPos)):
            # se genera de 1 a cromosomas -1 que seria abcd son 4 -1 son 3, NO PONGO -1 PORQUE COMO EMPIEZA EN 1 Y LA POSICION CUENTA COMO 0 SE EQUILIBRA
           # self.crossPoint[i] = np.random.randint(1, self.cromosomas.shape[1] ) No se porque me da error pero deberia de funcionar mientras dejare estatco con 3
           #self.crossPoint[i] = np.random.randint(1, 4 ) 
        #   self.crossPoint = np.random.randint(1, len(self.cromosomas[0]), size=len(self.cromosomas))
            primer_arreglo = self.cromosomas[0]
            self.crossPoint[i] = np.random.randint(1, primer_arreglo.shape[0])
           
            

        
    #recibe dos parametros la posicion de los cromosomas seleccionados y los puntos de cruze
    #tambien se requeriran los cromosomas
    def crossoverPoints(self):
        pos = self.parentPos
        point = self.crossPoint
        
        if len(pos) <= 1:
            return
    # NewChromosome = NewChromosome.astype(population.dtype) esto es solo de ejemplo
    # pos = pos.astype(self.cromosomas.dtype) #Este si funciona
        self.cromosomas = self.cromosomas.astype(int)
        pos = pos.astype(int)
        # Crear una copia temporal del arreglo porque si guardo en el principal los siguientes cruces tomaran los nuevos datos envez de los anteriores
        temp = np.copy(self.cromosomas)
        #lo qu hago es que para cada self.cromosomas que tomo de point(posiciones de self.cromosomass) le extraigo
        #cada gen que seria abcd, son diferentes ifs, en caso de que el punto de cruce sea 1
        #pues solo tomara 1 y los otros 3 del otro array, si son 2 pues toma 2 del primero y 2 del otro, 
        #y si sonn 3 pues toma 3 del primero y 1 del otro, PARA ESO SIRVEN LOS IFS(NOTA PERSONAL TRATAR DE IMPLEMENTARLO CON UN FOR PARA AHORRAR CODIGO)
        #primer cruce  Chromosome[1] >< Chromosome[4]
        
        for i in range(len(pos)):
            gen = np.empty(0)
            gen = np.append(gen, self.cromosomas.item(pos[i],0))
            punto = point
            punto = punto.astype(int)
            lenGen = self.cromosomas[0]
            #j = 1
            source = 1
            for j in range(1,lenGen.shape[0]):# -1 porque en la ultimia posicion se va a regresar, CREO QUE AQUI LO BOY A CAMBIAR HASTA EL TAMANO DE LOS GENES OSEA ABCD
                    if i == len(punto) - 1:#si es igual a la ultima psosicion regresa a comparar la primera
                        if j != point[i]:
                          gen = np.append(gen, self.cromosomas.item(pos[i],j))
                        else:
                          gen = np.append(gen, self.cromosomas.item(pos[0],j))
                          
                    elif source < point[i]:#AQUI LE TENGO QUE CAMBIAR ENTRO DENUEVO
                        gen = np.append(gen, self.cromosomas.item(pos[i],j))
                    else:
                        gen = np.append(gen, self.cromosomas.item(pos[i+1],j))
                        
                    source += 1
                        
                        #SOLO ENTRO 3 VECES      
            temp[pos[i]] = gen;   
      
        
        #MUEVO MI ARREGLO COPIA AL PRINCIPAL PARA REFLEJAR LOS CAMBIOS
        self.cromosomas = temp
        return self.cromosomas


        
        
        
   
    def mutationPoints(self):
        #------------------------------------------------------------------------
        #AQUI COMIENZA LO DE LA MUTACION
        #MAS ADELANTE PUEDO SACAR ESTO PARA HACER LOS PUNTOS DEPENDIENDO DE OTRA ESTRUCTURA
        #total_gen = number_of_gen_in_Chromosome * number of population
        #total_gen = 4 * 6           
        
        lenGen = self.cromosomas[0]
        
        total_gen = lenGen.shape[0] * self.cromosomas.shape[0]
        
        #Mutation process is done by generating a random integer between 1 and total_gen (1 to 24). 24 total de genes del cromosoma
        #Suppose we define ρm 10%, it is expected that 10% (0.1) of total_gen in the population that will be mutated
        number_of_mutations = 0.1 * total_gen
        #The value of mutated gens at mutation point is replaced by random number between 0-30.

        #------------------------------------------------------------------------
        #para poder iterar en number_of lo converitmos a int para que redonde el numero de mutaciones
        number_of_mutations = int(number_of_mutations)
        arrPosition = np.array([])
        arrCambios = np.array([])
        
        for i in range(number_of_mutations):
            #Este random es la posicion de lappoblacion que se reemplazara
            Rposition = np.random.randint(1,total_gen + 1)
            arrPosition = np.append(arrPosition, Rposition)
            
            #Este random es el numero por el cual se reemplazara 1 - 30
            Rcambio = np.random.randint(1,31)
            arrCambios = np.append(arrCambios, Rcambio)
            
            #AQUI HAGO EL INTERCAMBIO EN LA POSICION SELECCIONADA
            #np.place(cromosomas, cromosomas == Rposition -1, Rcambio)
            #PLACE NO ME FUNCIONO HAY QUE USAR PUT PORQUE SE ESPECIFICA LA POSICION SIN SABER EL IDNICE
            np.put(self.cromosomas,Rposition-1, Rcambio)
        #print("numero de mutaciones " + str(number_of_mutations)) REGRESAR EL VALOR ESTA DEMAS SOLO LO HAGO PARA PODER VERLO
        return self.cromosomas, arrPosition, arrCambios, number_of_mutations
    
        
    
    