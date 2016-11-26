# Adapted from code in Artificial Intelligence: A Modern Approach, by
### Russell and Norvig

# Note to students: please do not use the AIMA code for HW 2. Use this
# code instead. I've made some changes to the AIMA code to make it simpler
# and easier to work with. Using the AIMA code directly will just give you
# headaches.

import random

# global variable holding all possible agent actions
agent_actions = ['Left', 'Right', 'Suck', 'Up', 'Down']

# you should not need to change this code.


class Agent:
    """An Agent is a subclass of Object with one required slot,
    .program, which should hold a function that takes one argument, the
    percept, and returns an action. (What counts as a percept or action
    will depend on the specific environment in which the agent exists.) """
    a = 9

    def __init__(self):
        self.alive = True

    def program(percept):
        return raw_input('Percept=%s; action? ' % percept)


# a simple but stupid agent. Use this as a template when creating your own
# agents.
class RandomAgent(Agent):
    "An agent that chooses an action at random, ignoring all percepts."

    def __init__(self, actions):
        Agent.__init__(self)
        self.actions = actions

    def program(self, percept):
        action = random.choice(self.actions)
        print "Percept: %s Action: %s" % (percept, action)
        return action


# A slightly smarter agent - basically a reflex agent, this program just uses
# its current percepts to decide on an action.
class TableDrivenAgent(Agent):

    def __init__(self):
        Agent.__init__(self)

        # this is how our agent will determine what to do.
        # for every possible percept, we will look up in our
        # table (a dictionary) to find the correct action.

        # this will only work in 3x3 grids.

        # if the room is clean, we need to move
        self.actionTable = {((0, 0), 'Clean'): 'Right',
                            ((1, 0), 'Clean'): 'Right',
                            ((2, 0), 'Clean'): 'Up',
                            ((2, 1), 'Clean'): 'Up',
                            ((2, 2), 'Clean'): 'Left',
                            ((1, 2), 'Clean'): 'Left',
                            ((0, 2), 'Clean'): 'Down',
                            ((0, 1), 'Clean'): 'Down',
                            ((1, 1), 'Clean'): 'Down'}
        # if the room is dirty, let's clean it.
        for i in (0, 1, 2):
            for j in (0, 1, 2):
                self.actionTable[((i, j), 'Dirty')] = 'Suck'

        # this gives us a dictionary that maps room coordinates and state to an
        # action.

    def program(self, percept):
        # All we do is use the current percept to look up the correct
        # action in a table.

        print "Percept: %s Action: %s" % (percept, self.actionTable[percept])
        return self.actionTable[percept]


# A slightly smarter agent - basically a reflex agent, this program just uses
# its current percepts to decide on an action.
class ModelBasedAgent(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.statex = 0
        self.statey = 0
        self.action = ' '  # action
        self.size = (0, 0)
        self.state = 0
        self.sizex = 0
        self.sizey = 0
        self.i = 0
        self.j = 0
        self.k = 0
        self.originfound = False
        self.ready = False

    def origin(self, percept):
        # Walk to grid (0,0)
        self.statex, self.statey = percept[0]

        if self.statex != 0:
            self.action = 'Left'

        elif self.statey != 0:
            self.action = 'Down'

        if percept[0] == (0, 0):
            self.originfound = True

        return self.action

    def start(self, percept):
        # Count Grid size and go to starting position

        self.statex, self.statey = percept[0]

        if percept[1] == 'Dirty':
            self.action = 'Suck'

        elif self.statex >= 0 and self.statex == self.i:
            self.action = 'Right'
            self.i = self.i + 1

        elif self.statey >= 0 and self.statey == self.j:
            self.action = 'Up'
            self.j = self.j + 1

        elif percept[0] == (self.i - 1, self.j - 1):
            self.ready = True
            self.size = (self.statex, self.statey)
            self.i = self.i - 1
            self.j = self.j - 1

        return self.action

    def vacuumdown(self, percept):
        # Vacuum the enviroment

        self.statex, self.statey = percept[0]

        if percept[1] == 'Dirty':
            self.action = 'Suck'

        elif percept[0] == (0,0):
            self.ready = False
            self.i = 0
            self.j = 0

        elif self.statey == self.size[1]:
            if self.i >= self.statex:
                self.i -= 1
                self.action = 'Left'
            elif self.statex == 0:
                self.j -= 1
                self.action = 'Down'

        elif self.statey == self.j:
            if self.statex >= self.i:
                self.i += 1
                self.action = 'Right'

            elif self.statex == self.size[0]:
                self.j -= 1
                self.action = 'Down'

        elif self.statey >= self.j:
            if self.size[0] >= self.statex and self.statey >= self.j:
                self.j += 1
                self.action = 'Left'

        return self.action

    def program(self, percept):

        if self.originfound == False:
            self.origin(percept)

        elif self.ready == False:
            self.start(percept)

        elif self.ready == True:
            self.vacuumdown(percept)

        print "Percept: %s Action: %s" % (percept, self.action)

        return self.action

class NbyMVacuumEnvironment(Agent):

    def __init__(self, n=3, m=3):
        Agent.__init__(self)

        self.statex = 0
        self.statey = 0
        self.action = ' '  # action
        self.size = (0, 0)
        self.state = 0
        self.sizex = 0
        self.sizey = 0
        self.i = 0
        self.j = 0
        self.k = 0
        self.originfound = False
        self.ready = False

    def origin(self, percept):
        # Walk to grid (0,0)
        self.statex, self.statey = percept[0]

        if self.statex != 0:
            self.action = 'Left'

        elif self.statey != 0:
            self.action = 'Down'

        if percept[0] == (0, 0):
            self.originfound = True

        return self.action

    def start(self, percept):
        # Count Grid size and go to starting position

        self.statex, self.statey = percept[0]

        if percept[1] == 'Dirty':
            self.action = 'Suck'

        elif self.statex >= 0 and self.statex == self.i:
            self.action = 'Right'
            self.i = self.i + 1

        elif self.statey >= 0 and self.statey == self.j:
            self.action = 'Up'
            self.j = self.j + 1

        elif percept[0] == (self.i - 1, self.j - 1):
            self.ready = True
            self.size = (self.statex, self.statey)
            self.i = self.i - 1
            self.j = self.j - 1

        return self.action

    def vacuumdown(self, percept):
        # Vacuum the enviroment

        self.statex, self.statey = percept[0]

        if percept[1] == 'Dirty':
            self.action = 'Suck'

        elif percept[0] == (0,0):
            self.ready = False
            self.i = 0
            self.j = 0

        elif self.statey == self.size[1]:
            if self.i >= self.statex:
                self.i -= 1
                self.action = 'Left'
            elif self.statex == 0:
                self.j -= 1
                self.action = 'Down'

        elif self.statey == self.j:
            if self.statex >= self.i:
                self.i += 1
                self.action = 'Right'

            elif self.statex == self.size[0]:
                self.j -= 1
                self.action = 'Down'

        elif self.statey >= self.j:
            if self.size[0] >= self.statex and self.statey >= self.j:
                self.j += 1
                self.action = 'Left'

        return self.action

    def program(self, percept):

        if self.originfound == False:
            self.origin(percept)

        elif self.ready == False:
            self.start(percept)

        elif self.ready == True:
            self.vacuumdown(percept)

        print "Percept: %s Action: %s" % (percept, self.action)

        return self.action

    def percept(self, agent):
        "Returns the agent's location, and the location status (Dirty/Clean)."
        return (agent.location, self.status[agent.location])

    def printInitialState(self) :
        """ Show the initial problem state """
        print "Initial room config: ", self.status

    def printFinalState(self) :
        """ Show the final problem state """
        print "Final room config: ", self.status

    def default_location(self, object):
        "Agents start in any location at random."
        return random.choice(self.status.keys())

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        print "Location: %s Action: %s" % (agent.location, action)
        if not (action == 'Suck' or action == 'Noop') :
            ## if we moved, reduce performance by 1
            agent.performance -= 1
        if action == 'Suck' :
            ### if we suck up some dirt, we get 10 points
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'

        if action == 'Right':
            agent.location = (min(self.numRows - 1, agent.location[0] + 1),
                              agent.location[1])

        if action == 'Left' :
            agent.location = (max(0, agent.location[0] - 1), agent.location[1])


        if action == 'Up':
            agent.location = (agent.location[0],
                              min(self.numCols - 1, agent.location[1] + 1))

        if action == 'Down' :
            agent.location = (agent.location[0],
                              max(0, agent.location[1] - 1))
