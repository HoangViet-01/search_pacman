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
    """

    # Tạo ngăn xếp để lưu các trạng thái cần duyệt
    stack = util.Stack()

    # Lưu các trạng thái đã được duyệt
    visited = set()

    # Lấy trạng thái bắt đầu
    start_state = problem.getStartState()

    # Đưa trạng thái bắt đầu vào ngăn xếp
    stack.push((start_state, []))

    # Tiếp tục duyệt khi ngăn xếp còn phần tử
    while not stack.isEmpty():

        # Lấy trạng thái trên cùng và đường đi tương ứng
        state, actions = stack.pop()

        # Nếu trạng thái đã được duyệt thì bỏ qua
        if state in visited:
            continue

        # Đánh dấu trạng thái hiện tại là đã duyệt
        visited.add(state)

        # Nếu tìm thấy trạng thái đích thì trả về đường đi
        if problem.isGoalState(state):
            return actions

        # Lấy các trạng thái kế tiếp của trạng thái hiện tại
        for successor, action, stepCost in problem.getSuccessors(state):

            # Nếu trạng thái kế tiếp chưa được duyệt
            if successor not in visited:

                # Thêm trạng thái kế tiếp và đường đi mới vào ngăn xếp
                stack.push((successor, actions + [action]))

    # Không tìm thấy đường đi đến đích
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    # Tạo hàng đợi
    queue = util.Queue()

    # Lưu các trạng thái đã duyệt
    visited = set()

    # Lấy trạng thái bắt đầu
    start_state = problem.getStartState()

    # Thêm trạng thái bắt đầu vào hàng đợi
    queue.push((start_state, []))

    # Lặp khi hàng đợi còn phần tử
    while not queue.isEmpty():

        # Lấy trạng thái đầu tiên ra khỏi hàng đợi
        state, actions = queue.pop()

        # Nếu đã duyệt thì bỏ qua
        if state in visited:
            continue

        # Đánh dấu đã duyệt
        visited.add(state)

        # Nếu là trạng thái đích thì trả về đường đi
        if problem.isGoalState(state):
            return actions

        # Duyệt các trạng thái kế tiếp
        for successor, action, stepCost in problem.getSuccessors(state):

            # Nếu chưa duyệt thì thêm vào hàng đợi
            if successor not in visited:
                queue.push((successor, actions + [action]))

    # Không tìm thấy đường đi
    return []

def uniformCostSearch(problem: SearchProblem):
    # import PriorityQueue.
        from util import PriorityQueue
    
        pq = PriorityQueue()
        start_state = problem.getStartState()
        # (start_state, [], 0) : (vi tri hien tai, [cac huong da di chuyen tu start -> hien tai], tong gia tri khi di den o hien tai).
        pq.push((start_state, [], 0), 0) 
        visited = {} # Tao 1 dictionary (state, cost).
    
        while not pq.isEmpty():
            curr_state, actions, curr_cost = pq.pop()
            if curr_state in visited and visited[curr_state] <= curr_cost:
                continue
            visited[curr_state] = curr_cost
            # Kiem tra co phai Goal.
            if problem.isGoalState(curr_state):
                return actions
    
            for next_state, next_action, next_cost in problem.getSuccessors(curr_state):
                new_action = actions + [next_action]
                new_cost = curr_cost + next_cost
    
                if next_state not in visited or visited[next_state] < new_cost:
                    pq.push((next_state, new_action, new_cost), new_cost) # Do uu tien trong pq : cost.
    
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
