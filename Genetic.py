"""
PROJECT HEADER GOES HERE
"""
import random
#DO NOT CHANGE THIS
random.seed(10)

NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer! 
This program will attempt to guess a sentence that you input. 
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

INPUT = "\nWould you like to continue? (y/n) "

"\nPlease input the sentence you would like the program to guess: "
"\nIncorrect input. Please try again.\n"
"\n\nGeneticGuess results:"
"Generation: "
"I found the sentence early!"
"\nBest Individual: "
"\n\nThank you for using GeneticGuess Sentencer!"


def fitness(target, individual):
    fitness_count = 0.0
    for i in range(0,len(target)):
        if (target[i] == individual[i]):
            fitness_count += 1
    fitness_count /= len(target)
    return fitness_count

def five_tournament_selection(population, target):
    max_fitness = -1.0
    temp_fitness= 0.0
    best_individual=population[0:len(target)]
    for i in range(0,5):
        ind = random.randint(0, NUM_POPULATION - 1)*len(target)
        individual = population[ind:ind+len(target)]
        temp_fitness = fitness(target,individual)
        if (temp_fitness > max_fitness):
            max_fitness = temp_fitness
            best_individual = individual
    return best_individual


def make_population(target):
    n=len(target)#length of an individual 
    x=""#random letter
    population=""#population
    for i in range(0,(NUM_POPULATION*n)):#length of total population
        x=random.choice(ALPHABET)
        population=population+x
    return population


def mutation(individual):
    chosen_number=""
    newindividual=""
    for i in range(0,len(individual)):
        chosen_number=random.random()
        if(chosen_number<PROBABILITY_MUTATION):
            newindividual=newindividual+random.choice(ALPHABET)
        else:
            newindividual=newindividual+individual[i]
    return newindividual


def single_point_crossover(individual1, individual2):
    newindividual1=""
    newindividual2=""
    check=0.0
    check=random.random()
    if(check>PROBABILITY_CROSSOVER):
        return individual1,individual2
    else:
        a=len(individual1)
        point_to_crossover=random.randint(1,a)
        newindividual1=individual1[:point_to_crossover] + individual2[point_to_crossover:]
        newindividual2=individual2[:point_to_crossover] + individual1[point_to_crossover:]
    return newindividual1,newindividual2
    
def find_best_individual(population, target):
    temp=0.0
    max_fit=-1.0
    best_individual=""
    start=0
    for i in range(0,NUM_POPULATION):
        start=i*len(target)
        individual=population[start:start+len(target)]
        temp=fitness(target,individual)
        if(temp>max_fit):
            max_fit=temp
            best_individual=individual
    return best_individual


def main():
    populationf=""
    ind1=""
    ind2=""
    f1=0.0
    f2=0.0
    print(BANNER)
    input1=input(INPUT)
    while(input1.lower()=="y"):
        inputf=(input("\nPlease input the sentence you would like the program to guess: ")).lower()
        input1=""
        while any(char not in ALPHABET for char in inputf):
            print("Invalid input. Please use only alphabets and space.")
            inputf = input("Please input the sentence you would like the program to guess: ").lower()
        newpopulation= make_population(inputf)
        for i in range(0,NUM_GENERATIONS):
            print("Generation: ",i+1)
            populationf=newpopulation #np
            newpopulation=""
            breakcounter=0
            for j in range(0,NUM_POPULATION):
                ind1=five_tournament_selection(populationf,inputf)#finding 2 individuals 
                ind2=five_tournament_selection(populationf,inputf)#finding 2 individuals
                ind1=mutation(ind1)#mutating
                ind2=mutation(ind2)#mutating
                ind1,ind2=single_point_crossover(ind1, ind2)#single point crossover
                f1=fitness(inputf,ind1)
                f2=fitness(inputf,ind2)
                if(fitness(inputf,ind1)==1):
                    print("I found the sentence early!","\nBest Individual: ",ind1,"\n\nThank you for using GeneticGuess Sentencer!")
                    breakcounter +=1
                    break
                elif(fitness(inputf,ind2)==1):
                    print("I found the sentence early!","\n\nBest Individual: ",ind2,"\n\nThank you for using GeneticGuess Sentencer!")
                    breakcounter +=1
                    break
                elif(fitness(inputf,ind1)>=fitness(inputf,ind2)):
                    newpopulation+=ind1
                elif(fitness(inputf,ind2)>fitness(inputf,ind1)):
                    newpopulation+=ind2
            if(breakcounter==1):
                break
        input1=input(INPUT)#e
    print("\n\nThank you for using GeneticGuess Sentencer!")
    return
            
            
        

# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()
