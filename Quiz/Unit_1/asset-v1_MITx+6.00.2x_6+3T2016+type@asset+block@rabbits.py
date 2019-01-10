import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300



#CURRENTRABBITPOP = 10
#CURRENTFOXPOP = 20
#MAXRABBITPOP = 100
def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    currRabbit = CURRENTRABBITPOP
    for i in range(currRabbit):
        if CURRENTRABBITPOP <= MAXRABBITPOP:
            if (1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)) > random.random():
                CURRENTRABBITPOP += 1
        else:
            break
        
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    currFox = CURRENTFOXPOP
    for i in range(currFox):
        if CURRENTRABBITPOP/float(MAXRABBITPOP) > random.random() and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() < (1/float(3)) and CURRENTFOXPOP < CURRENTRABBITPOP:
                CURRENTFOXPOP += 1
            else:
                if random.random() > 0.1 and CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for i in range(numSteps):
        if CURRENTFOXPOP > 10 and CURRENTRABBITPOP > 10:
            rabbitGrowth()
            foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations, fox_populations)

rabbit, fox = runSimulation(200)
coeff = pylab.polyfit(range(len(rabbit)), rabbit, 2)
coeff2 = pylab.polyfit(range(len(fox)), fox, 2)
pylab.figure()
pylab.plot(pylab.polyval(coeff, range(len(rabbit))))
pylab.plot(pylab.polyval(coeff2, range(len(rabbit))))
#pylab.plot(range(len(rabbit)), rabbit)
#pylab.plot(range(len(rabbit)), fox)
pylab.legend('best')
pylab.show()
