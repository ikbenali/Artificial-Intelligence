### Adapted from code in Artificial Intelligence: A Modern Approach, by
### Russell and Norvig

### Note to students: please do not use the AIMA code for HW 2. Use this
### code instead. I've made some changes to the AIMA code to make it simpler
### and easier to work with. Using the AIMA code directly will just give you
#### headaches.

import random

### global variable holding all possible agent actions
agent_actions = ['Left', 'Right', 'Suck', 'Up', 'Down']

### you should not need to change this code.
class Agent :
    """An Agent is a subclass of Object with one required slot,
    .program, which should hold a function that takes one argument, the
    percept, and returns an action. (What counts as a percept or action
    will depend on the specific environment in which the agent exists.) """

    def __init__(self): 
        self.alive = True

    def program(percept):
            return raw_input('Percept=%s; action? ' % percept)


### a simple but stupid agent. Use this as a template when creating your own agents.
class RandomAgent(Agent):
    "An agent that chooses an action at random, ignoring all percepts."
    def __init__(self, actions):
        Agent.__init__(self)
        self.actions = actions

    def program(self, percept) :
        action = random.choice(self.actions)
        print ("Percept: %s Action: %s" % (percept, action))
        return action


### A slightly smarter agent - basically a reflex agent, this program just uses 
### its current percepts to decide on an action.
class TableDrivenAgent(Agent) :

    def __init__(self) :
        Agent.__init__(self)

        ### this is how our agent will determine what to do.
        ### for every possible percept, we will look up in our
        ### table (a dictionary) to find the correct action.
        
        ### this will only work in 3x3 grids.

        ### if the room is clean, we need to move
        self.actionTable = {((0,0), 'Clean') : 'Right',
                            ((1,0), 'Clean') : 'Right',
                            ((2,0), 'Clean') : 'Up',
                            ((2,1), 'Clean') : 'Up',
                            ((2,2), 'Clean') : 'Left',
                            ((1,2), 'Clean') : 'Left',
                            ((0,2), 'Clean') : 'Down',
                            ((0,1), 'Clean') : 'Down',
                            ((1,1), 'Clean') : 'Down'}
        ### if the room is dirty, let's clean it.
        for i in (0,1,2) :
            for j in (0,1,2) :
                self.actionTable[((i,j), 'Dirty')] = 'Suck'
        ### this gives us a dictionary that maps room coordinates and state to an action.

    
    def program(self, percept) :
        ### All we do is use the current percept to look up the correct
        ### action in a table.
        print ("Percept: %s Action: %s" % (percept, self.actionTable[percept]))
        return self.actionTable[percept]



        
        

        
