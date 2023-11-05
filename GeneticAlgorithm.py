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
        F_obj[0] = abs((self.cromosomas[0,0] + (self.cromosomas[0,1] * 2) + (self.cromosomas[0,2] * 3) + (self.cromosomas[0,3] * 4)) - 30)
        F_obj[1] = abs((self.cromosomas[1,0] + (self.cromosomas[1,1] * 2) + (self.cromosomas[1,2] * 3) + (self.cromosomas[1,3] * 4)) - 30)
        F_obj[2] = abs((self.cromosomas[2,0] + (self.cromosomas[2,1] * 2) + (self.cromosomas[2,2] * 3) + (self.cromosomas[2,3] * 4)) - 30)
        F_obj[3] = abs((self.cromosomas[3,0] + (self.cromosomas[3,1] * 2) + (self.cromosomas[3,2] * 3) + (self.cromosomas[3,3] * 4)) - 30)
        F_obj[4] = abs((self.cromosomas[4,0] + (self.cromosomas[4,1] * 2) + (self.cromosomas[4,2] * 3) + (self.cromosomas[4,3] * 4)) - 30)
        F_obj[5] = abs((self.cromosomas[5,0] + (self.cromosomas[5,1] * 2) + (self.cromosomas[5,2] * 3) + (self.cromosomas[5,3] * 4)) - 30)
        return F_obj
        
    #PASO 3: FUNCION FITNESS
    def fitnessFunction(self):
        #Fitness[1] = 1 / (1+F_obj[1]) EJEMPLO
        functionResult = self.objectiveFunction()
        Fitness = np.zeros(functionResult.shape)
        Fitness[0] = 1 / (1+functionResult[0])
        Fitness[1] = 1 / (1+functionResult[1])
        Fitness[2] = 1 / (1+functionResult[2])
        Fitness[3] = 1 / (1+functionResult[3])
        Fitness[4] = 1 / (1+functionResult[4])
        Fitness[5] = 1 / (1+functionResult[5])
        
        total = Fitness[0]+Fitness[1]+Fitness[2]+Fitness[3]+Fitness[4]+Fitness[5]
        return Fitness, total
    

    def probabilityFunction(self):
        #P[i] = Fitness[i] / Total EJEMPLO
        #fitnessResult = self.fitnessFunction
        fitness = self.fitnessFunction()[0]
        total = self.fitnessFunction()[1]
        P = np.zeros(fitness.shape)
        P[0] = fitness[0] / total
        P[1] = fitness[1] / total
        P[2] = fitness[2] / total
        P[3] = fitness[3] / total
        P[4] = fitness[4] / total
        P[5] = fitness[5] / total
        return P

    def probabilityComulative(self):
        p = self.probabilityFunction()
        #C[i] = 0.1254 + n
        C = np.zeros(p.shape)
        C[0] = p[0]
        C[1] = p[0] + p[1]
        C[2] = p[0] + p[1] + p[2]
        C[3] = p[0] + p[1] + p[2] + p[3]
        C[4] = p[0] + p[1] + p[2] + p[3] + p[4]
        C[5] = p[0] + p[1] + p[2] + p[3] + p[4] + p[5]
        return C
     

    def comparacionesRandom(self):
        NewChromosome = np.zeros(self.cromosomas.shape)
        self.nRandom = np.random.rand(6)
        #self.nRandom = np.array([[0.201],[0.284],[0.099],[0.822],[0.398],[0.501]])

        #for i in range(0, 6):
        for i in range(len(self.cromosomas)):

            if self.nRandom[i] > self.probabilityComulative()[0] and self.nRandom[i] < self.probabilityComulative()[1]:
                NewChromosome[i] = self.cromosomas[1]
                print(f"NewChromosome[{i}] PosA[{2}] = [a; b; c; d] = {NewChromosome[i]}")
                
            elif self.nRandom[i] > self.probabilityComulative()[1] and self.nRandom[i] < self.probabilityComulative()[2]:
                NewChromosome[i] = self.cromosomas[2]
                print(f"NewChromosome[{i}] PosA[{3}] = [a; b; c; d] = {NewChromosome[i]}")
                
            elif self.nRandom[i] > self.probabilityComulative()[2] and self.nRandom[i] < self.probabilityComulative()[3]:
                NewChromosome[i] = self.cromosomas[3]
                print(f"NewChromosome[{i}] PosA[{4}] = [a; b; c; d] = {NewChromosome[i]}")
                
            elif self.nRandom[i] > self.probabilityComulative()[3] and self.nRandom[i] < self.probabilityComulative()[4]:
                NewChromosome[i] = self.cromosomas[4]
                print(f"NewChromosome[{i}] PosA[{5}] = [a; b; c; d] = {NewChromosome[i]}")
                
            elif self.nRandom[i] > self.probabilityComulative()[4] and self.nRandom[i] < self.probabilityComulative()[5]:
                NewChromosome[i] = self.cromosomas[5]
                print(f"NewChromosome[{i}] PosA[{6}] = [a; b; c; d] = {NewChromosome[i]}")
                
            elif self.nRandom[i] < self.probabilityComulative()[0]:
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

        pc = .25
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
           self.crossPoint[i] = np.random.randint(1, 4 ) 
           
            

        
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
        if len(pos) == 2:
            pointC1 = point[0]
            pointC2 = point[1]
        
            
            gen1 = self.cromosomas.item(pos[0],0)
            if pointC1 == 1:
                gen2 = self.cromosomas.item(pos[0+1],1)
                gen3 = self.cromosomas.item(pos[0+1],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            elif pointC1 == 2:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0+1],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            elif pointC1 == 3:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            
            temp[pos[0]] = [gen1, gen2, gen3, gen4]
            #self.cromosomas[pos[0]] = [gen1,gen2,gen3,gen4]
            #segundo cruce Chromosome[4] >< Chromosome[5]
            gen1 = self.cromosomas.item(pos[1],0)
            if pointC2 == 1:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0],3)
            elif pointC2 == 2:
                gen2 = self.cromosomas.item(pos[1],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0],3)
            elif pointC2 == 3:
                gen2 = self.cromosomas.item(pos[1],1)
                gen3 = self.cromosomas.item(pos[1],2)
                gen4 = self.cromosomas.item(pos[0],3)
                
            temp[pos[1]] = [gen1, gen2, gen3, gen4]
                
            #-------------
        else:
            pointC1 = point[0]
            pointC2 = point[1]
            pointC3 = point[2]
            
            gen1 = self.cromosomas.item(pos[0],0)
            if pointC1 == 1:
                gen2 = self.cromosomas.item(pos[0+1],1)
                gen3 = self.cromosomas.item(pos[0+1],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            elif pointC1 == 2:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0+1],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            elif pointC1 == 3:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0+1],3)
            
            temp[pos[0]] = [gen1, gen2, gen3, gen4]
            #self.cromosomas[pos[0]] = [gen1,gen2,gen3,gen4]
            #segundo cruce Chromosome[4] >< Chromosome[5]
            gen1 = self.cromosomas.item(pos[1],0)
            if pointC2 == 1:
                gen2 = self.cromosomas.item(pos[1+1],1)
                gen3 = self.cromosomas.item(pos[1+1],2)
                gen4 = self.cromosomas.item(pos[1+1],3)
            elif pointC2 == 2:
                gen2 = self.cromosomas.item(pos[1],1)
                gen3 = self.cromosomas.item(pos[1+1],2)
                gen4 = self.cromosomas.item(pos[1+1],3)
            elif pointC2 == 3:
                gen2 = self.cromosomas.item(pos[1],1)
                gen3 = self.cromosomas.item(pos[1],2)
                gen4 = self.cromosomas.item(pos[1+1],3)
                
            temp[pos[1]] = [gen1, gen2, gen3, gen4]
            #self.cromosomas[pos[1]] = [gen1,gen2,gen3,gen4]
            
            #tecer cruce Chromosome[5] >< Chromosome[1]
            gen1 = self.cromosomas.item(pos[2],0)
            if pointC3 == 1:
                gen2 = self.cromosomas.item(pos[0],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0],3)
            elif pointC3 == 2:
                gen2 = self.cromosomas.item(pos[2],1)
                gen3 = self.cromosomas.item(pos[0],2)
                gen4 = self.cromosomas.item(pos[0],3)
            elif pointC3 == 3:
                gen2 = self.cromosomas.item(pos[2],1)
                gen3 = self.cromosomas.item(pos[2],2)
                gen4 = self.cromosomas.item(pos[0],3)
            
            #self.cromosomas[pos[2]] = [gen1,gen2,gen3,gen4]
            temp[pos[2]] = [gen1, gen2, gen3, gen4]
        
        #MUEVO MI ARREGLO COPIA AL PRINCIPAL PARA REFLEJAR LOS CAMBIOS
        self.cromosomas = temp
        return self.cromosomas


        
        
        
   
    def mutationPoints(self):
        #------------------------------------------------------------------------
        #AQUI COMIENZA LO DE LA MUTACION
        #MAS ADELANTE PUEDO SACAR ESTO PARA HACER LOS PUNTOS DEPENDIENDO DE OTRA ESTRUCTURA
        #total_gen = number_of_gen_in_Chromosome * number of population
        total_gen = 4 * 6           
        
        #Mutation process is done by generating a random integer between 1 and total_gen (1 to 24). 24 total de genes del cromosoma
        #Suppose we define ρm 10%, it is expected that 10% (0.1) of total_gen in the population that will be mutated
        number_of_mutations = 0.1 * 24
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
    
        
    
    