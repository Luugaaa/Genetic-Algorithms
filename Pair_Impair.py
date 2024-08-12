class Individu:
    def __init__(self,numero_population,p1):
        self.p1=p1;
        self.p2=1-p1;
        self.numero_population=numero_population;
    def esperance_gain(self,individu2):
        if self.numero_population==1:
            return (self.p1-self.p2)*(individu2.p1-individu2.p2)
        else:
            return -(self.p1-self.p2)*(individu2.p1-individu2.p2)


def initialisation(taille_population):
    population1=[Individu(1,rand()) for i in range(taille_population)];
    population2=[Individu(2,rand()) for i in range(taille_population)];
    esperances1=[sum([individu1.esperance_gain(individu2) for individu2 in population2]) for individu1 in population1];
    esperances2=[sum([individu2.esperance_gain(individu1) for individu1 in population1]) for individu2 in population2];
    meilleur1=esperances1.index(max(esperances1));
    meilleur2=esperances2.index(max(esperances2));
    return (population1,meilleur1,population2,meilleur2)


def trouver_meilleur_et_pire(population1,meilleur1,population2,meilleur2):
    esperances_de_gain1=[individu1.esperance_gain(population2[meilleur2]) for individu1 in population1];
    esperances_de_gain2=[individu2.esperance_gain(population1[meilleur1]) for individu2 in population2];
    meilleur1=esperances_de_gain1.index(max(esperances_de_gain1));
    pire1=esperances_de_gain1.index(min(esperances_de_gain1));
    meilleur2=esperances_de_gain2.index(max(esperances_de_gain2));
    pire2=esperances_de_gain2.index(min(esperances_de_gain2));
    return (meilleur1,pire1,meilleur2,pire2)

def mutation(meilleur_individu,numero_population,em):
    nouveau_p1=uniform(max(meilleur_individu.p1-em,0),min(meilleur_individu.p1+em,1));
    return Individu(numero_population,nouveau_p1)


def algorithme_genetique(Npop,em,nombre_iterations):
    population1,meilleur1,population2,meilleur2=initialisation(Npop);
    population1_esperance=[];
    population2_esperance=[];
    for k in range(nombre_iterations):
        meilleur1,pire1,meilleur2,pire2=trouver_meilleur_et_pire(population1,meilleur1,population2,meilleur2);
        population1[pire1]=mutation(population1[meilleur1],1,em);
        population2[pire2]=mutation(population2[meilleur2],2,em);
        population1_esperance.append(population1[meilleur1].esperance_gain(population2[meilleur2]));
        population2_esperance.append(population2[meilleur2].esperance_gain(population1[meilleur1]));
    temps=list(range(nombre_iterations));
    plot(temps,population1_esperance,'blue',temps,population2_esperance,'red');
    return population1[meilleur1].p1,population1[meilleur1].p2

Npop=10;
em=0.03;
nombre_iterations=500;

print(algorithme_genetique(Npop,em,nombre_iterations));