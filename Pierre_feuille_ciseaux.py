import numpy as np
import matplotlib.pyplot as plt

class individu:
    def __init__(self, nom, proba, fitness):
        self.nom = nom
        self.proba = proba
        self.fitness = fitness
    def __repr__(self):
        return repr((self.nom, self.proba, self.fitness))

def FitnessBase(p1,p2):
    result=1.0*p1*p2 + 1.0*(1.0-p1)*(1.0-p2) - 1.0*p1*(1.0-p2) - 1.0*(1.0-p1)*p2
    return result


def FitnessP1ContreP2(p1,p2):
    result = []
    
    for x in p1:
        x.fitness=FitnessBase(x.proba,p2.proba)
    result=sorted(p1, key=lambda individu: individu.fitness)

    return result    

def FitnessP2ContreP1(p1,p2):
    result = []
    
    for x in p2:
        x.fitness=-FitnessBase(p1.proba,x.proba)
    result=sorted(p2, key=lambda individu: individu.fitness)

    return result    


def Evolution(population):
    em=.01
    pM=.01
    pm=.5
    ps=.3
    #np.random.randint(len(population)-3, len(population)-1)
    
    rr=np.floor(len(population)*(1-ps-pM-pm))

    for i in range(0,len(population)-1):             
        if i < pM*len(population)-1:
            population[i].proba = np.random.rand()
            
        elif i < (pM+ps)*len(population)-1:
            meilleur=population[np.random.randint(len(population)-rr, len(population)-1)]
            population[i].proba = (population[i].proba + meilleur.proba)/2.0    

        elif i < (pM+pm+ps)*len(population)-1:
            meilleur=population[np.random.randint(len(population)-rr, len(population)-1)]
            population[i].proba = min(max(meilleur.proba + np.random.uniform(-em,em),0.0),1.0)

        
    #population[-1]=meilleur
    
    
    return population

  


def gene(temps=5000, N=50):

    fitnessmax1=[]
    probamax1=[]
    fitnessmax2=[]
    probamax2=[]
    
    Population1=[];
    Population2=[];

### On initialise la population
    for n in range(N):
        x = np.random.rand()
        y = np.random.rand()
        Population1.append(individu('P1', x, 0))
        Population2.append(individu('P2', y, 0))
 
 ### On cherche d'une facon ou d'une autre un meilleur a l'etape 0 (ici en moyenne)     
    for x in Population1:
        for y in Population2:
            x.fitness=x.fitness+FitnessBase(x.proba,y.proba)

    for x in Population2:
        for y in Population1:
            x.fitness=x.fitness-FitnessBase(y.proba,x.proba)

    Population1=sorted(Population1, key=lambda individu: individu.fitness)
    Population2=sorted(Population2, key=lambda individu: individu.fitness)

    
    #au temps k
    for k in range(temps):

        best1=Population1[-1]        
        best2=Population2[-1]        

        Population1=FitnessP1ContreP2(Population1,best2)
        Population1=Evolution(Population1)

        Population2=FitnessP2ContreP1(best1,Population2)
        Population2=Evolution(Population2)        

                
        fitnessmax1.append(best1.fitness)
        fitnessmax2.append(best2.fitness)
        probamax1.append(best1.proba)
        probamax2.append(best2.proba)
        
    
    fig, ax = plt.subplots()
    ax.plot(probamax1)
    ax.plot(probamax2)   
    plt.show()
    print(best1)
    print(best2)
    
   
    
    return fitnessmax1,fitnessmax2,probamax1,probamax2

gene()
#print(gene())

#test(25)