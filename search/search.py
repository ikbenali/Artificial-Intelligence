# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(), None, 0, None)

    if problem.isGoalState(node):
        return node.sol

    frontier = [node]
    explored = []

    while True:
        if not frontier:
            util.raiseNotDefined()
        node = frontier.pop(0)
        explored.append(node.state)
        children = []

        for c in problem.getSuccessors(node.state):
            child = Node(c[0], c[1], c[2], node)
            # print "Node(%s, %s, %s, %s)" % (child.state, child.action,
            # child.cost, node.state)
            if child not in frontier and child.state not in explored:
                if problem.isGoalState(child.state):
                    return Node.sol(child)
                children.append(child)
        frontier = children + frontier


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(), None, 0, None)

    # if problem.isGoalState(node): # set to comment, otherwise it will not work with eightpuzzle.py
    #    return node.sol
    frontier = util.Queue()
    frontier.push(node)
    explored = []

    while True:
        if frontier.isEmpty == 1:
            util.raiseNotDefined()
        node = frontier.pop()
        explored.append(node.state)
        for c in problem.getSuccessors(node.state):
            child = Node(c[0], c[1], c[2], node)
            # print "Node(%s, %s, %s, %s)" % (child.state, child.action,
            # child.cost, node.state)
            if child not in frontier.list and child.state not in explored:
                if problem.isGoalState(child.state):
                    return Node.sol(child)
                frontier.push(child)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(), None, 0, None)

    # set to comment, otherwise it will not work with eightpuzzle.py
    if problem.isGoalState(node):
        return node.sol
    frontier = util.PriorityQueue()
    frontier.push(node, node.cost)
    explored = []

    while True:
        if frontier.isEmpty == 1:
            util.raiseNotDefined()

        node = frontier.pop()
        if problem.isGoalState(node.state):
            return Node.sol(node)
        explored.append(node.state)
        for c in problem.getSuccessors(node.state):
            child = Node(c[0], c[1], c[2], node)
            if child not in frontier.heap and child.state not in explored:
                frontier.push(child, child.cost)

            elif child.state in frontier.heap is child.state > frontier.heap:
                frontier.push(child, child.cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState(), None, 0, None)

    # set to comment, otherwise it will not work with eightpuzzle.py
    if problem.isGoalState(node):
        return node.sol
    frontier = util.PriorityQueue()
    frontier.push(node, (node.cost + heuristic(node.state,problem)))
    explored = []

    while True:
        if frontier.isEmpty == 1:
            util.raiseNotDefined()

        node = frontier.pop()
        if problem.isGoalState(node.state):
            return Node.sol(node)
        explored.append(node.state)
        for c in problem.getSuccessors(node.state):
            child = Node(c[0], c[1], c[2], node)
            if child not in frontier.heap and child.state not in explored:
                frontier.push(child, (child.cost + heuristic(child.state,problem)))
            elif child.state in frontier.heap is child.state > frontier.heap:
                frontier.push(child, child.cost)

class Node:

    def __init__(self, s, a, c, p):
        self.state = s
        self.action = a
        self.cost = c
        self.parent = p

    # def __repr__(self):
    # return "Node(%s, %s, %s, %s)" % (self.state, self.action, self.cost,
    # self.parent)

    def sol(self):
        if self.parent is None:
            return []
        else:
            return self.parent.sol() + [self.action]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
