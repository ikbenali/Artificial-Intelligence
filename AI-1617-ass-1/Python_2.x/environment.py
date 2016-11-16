### Adapted from code in Artificial Intelligence: A Modern Approach, by
### Russell and Norvig

### Note to students: please do not use the AIMA code for HW 2. Use this
### code instead. I've made some changes to the AIMA code to make it simpler
### and easier to work with. Using the AIMA code directly will just give you
#### headaches.


import random

class Environment:
    """Abstract class representing an Environment.  'Real' Environment classes
    inherit from this. Your Environment will typically need to implement:
        percept:           Define the percept that an agent sees.
        execute_action:    Define the effects of executing an action.
                           Also update the agent.performance slot.
    The environment keeps a list of .objects and .agents (which is a subset
    of .objects). Each agent has a .performance slot, initialized to 0.
    Each object has a .location slot, even though some environments may not
    need this."""

    def __init__(self,):
        self.objects = []
        self.agents = []

        object_classes = [] ## List of classes that can go into environment

    ### note: abstract() is a placeholder that requires subclasses to implement
    ### this method if they want to inherit from this class. It provides a
    ### mechanism similar to the use of virtual in C++, or interfaces in Java.

    def percept(self, agent):
	"Return the percept that the agent sees at this point. Override this."
        abstract()

    def execute_action(self, agent, action):
        "Change the world to reflect this action. Override this."
        abstract()

    def default_location(self, object):
	"Default location to place a new object with unspecified location."
        return None

    ### pass is a statement that means 'do nothing' - unlike abstract,
    ### subclasses are not required to override this method.

    def exogenous_change(self):
	"If there is spontaneous change in the world, override this."
	pass

    def is_done(self):
        "By default, we're done when we can't find a live agent."
        return False

    def step(self):
	"""Run the environment for one time step. If the
	actions and exogenous changes are independent, this method will
	do.  If there are interactions between them, you'll need to
	override this method."""
	if not self.is_done():
            ### for each agent, give them a percept and get the resulting
            ### action.
            actions = [agent.program(self.percept(agent))
                       for agent in self.agents]
            ### apply all actions to the environment
            for (agent, action) in zip(self.agents, actions):
		self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
	"""Run the Environment for given number of time steps."""
        self.printInitialState()
        for step in range(steps):
            if self.is_done():
                self.printFinalState()
                return
            self.step()
        self.printFinalState()

    def printInitialState(self) :
            """ Show the initial problem state """
            pass

    def printFinalState(self) :
        """ Show the final problem state """
        pass

    def add_object(self, object, location=None):
	"""Add an object to the environment, setting its location. Also keep
	track of objects that are agents.  Shouldn't need to override this."""
	object.location = location or self.default_location(object)
	self.objects.append(object)
	if isinstance(object, Agent):
            object.performance = 0
            self.agents.append(object)
	return self

    def add_agent(self, ag, location=None) :
        """Add an agent to the environment"""
        ag.location = location or self.default_location(ag)
        ag.performance = 0
        self.agents.append(ag)
	return self


### I'll derive NbyMVacuumEnvironment from Environment
### Notice that the default size for the grid is 3x3 - to get other sizes,
### provide optional arguments to the constructor.

class NbyMVacuumEnvironment(Environment) :
    def __init__(self, n=3, m=3):
        Environment.__init__(self)
        self.status = {}
        self.numRows = n
        self.numCols = m
        for i in range(0,n) :
            for j in range(0,m) :
                self.status[(i,j)] = random.choice(['Clean', 'Dirty'])

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
