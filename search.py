# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    visit = set()
    start_s = problem.getStartState()
    stack.push((start_s,[]))

    while not stack.isEmpty():
        state,actions = stack.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visit:
            visit.add(state)
            for successor, action,cost in problem.getSuccessors(state):
                if successor not in visit:
                    stack.push((successor,actions + [action]))

    
    return []

    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    que = util.Queue()
    visit = set()
    start_s = problem.getStartState()
    que.push((start_s,[]))

    while not que.isEmpty():
        state,actions = que.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visit:
            visit.add(state)
            for successor, action,cost in problem.getSuccessors(state):
                if successor not in visit:
                    que.push((successor,actions + [action]))

    
    return []


    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # ucs 알고리즘 (현재까지 cost + 앞으로 들 cost)....가장 적은 비용 

    #  UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    #  initialize the explored set to be empty
    #  initialize the frontier as a priority queue using node path_cost as the priority
    #  add initial state of problem to frontier with path_cost = 0
    #  loop do
    #  if the frontier is empty then
    #  return failure
    #  choose a node and remove it from the frontier
    #  if the node contains a goal state then
    #  return the corresponding solution
    #  add the node state to the explored set
    #  for each resulting child from node
    #  if the child state is not already in the frontier or explored set then
    #  add child to the frontier
    #  else if the child is already in the frontier with higher path_cost then
    #  replace that frontier node with child

    visit = set()
    front = util.PriorityQueue()
    start_s = problem.getStartState()
    # cost,action,node
    front.push((0,[],start_s),0)

    while not front.isEmpty():
        cost,actions,node = front.pop()

        if problem.isGoalState(node):
            return actions

        if node not in visit:
            visit.add(node)
            for successor, action,cost1 in problem.getSuccessors(node):
                if successor not in visit:
                    cost2 = cost + cost1
                    actions1 = actions + [action]
                    # cost,action,node
                    front.push((cost2,actions1,successor),cost2) 

    return []
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # function A-STAR-SEARCH(problem) returns a solution, or failure
    # initialize the explored set to be empty
    # initialize the frontier as a priority queue using 𝒇(𝒏) = 𝒈(𝒏) + 𝒉(𝒏) as the priority
    # add initial state of problem to frontier with priority 𝒇(𝑺) = 𝟎 + 𝒉(𝑺)
    # loop do
    # if the frontier is empty then
    # return failure
    # choose a node and remove it from the frontier
    # if the node contains a goal state then    
    # return the corresponding solution
    # add the node state to the explored set
    # for each resulting child from node
    # if the child state is not already in the frontier or explored set then
    # add child to the frontier
    # else if the child is already in the frontier with higher 𝒇(𝒏) then
    # replace that frontier node with child


    visit = set()
    front = util.PriorityQueue()
    start_s = problem.getStartState()
    front.push((start_s,[],0),(start_s,problem))

    while not front.isEmpty():
        node,actions,cost = front.pop()
        if problem.isGoalState(node):
            return actions
        if node not in visit:
            visit.add(node)
            for successor,action,cost1 in problem.getSuccessors(node):
                action1 = actions +[action]
                cost2 = cost + cost1
                pri = cost2 + heuristic(successor,problem)
                front.update((successor,action1,cost2),pri)
    return 

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
