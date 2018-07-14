from heapq import heappush, heappop
import time
from math import*


class Search:
    def __init__(self, initial_state=None):
        self.initial_state = Node(initial_state)
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def uniform_cost(self):
        return self.cost()

    def misplaced(self):
        return sum([1 if self.numbers[i] != self.goal[i] else 0 for i in xrange(8)])

    def man_dist(self):
        goal_state =[1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(abs(a - b) for a, b in zip(self.numbers, goal_state))

    def reconstruct_path(self, end):
        path = [end]
        state = end.parent
        while state.parent:
            path.append(state)
            state = state.parent
        return path

    def search(self, heuristic):
        # Initialize Open List to store the nodes yet to be explored
        open = Queue()
        # Add the initial state to the Open List
        open.add(self.initial_state)
        # Initialize the closed list which stores the nodes already visited
        closed = set()
        moves = 0
        print ('\nInitial State:')
        print (open.peek())
        print('\n')
        start = time.time()
        overall_count = 0
        #Until the open list has nodes to be explored
        while open:
            # Retrieve the head of the open list
            current = open.head()
            if current.numbers[:-1] == self.goal:
                # Start timer if the initial state has not yet reached the goal state
                end = time.time()
                print('The given puzzle is solvable')
                path = self.reconstruct_path(current)
                # Path is reversed to obtain the path from initial state
                for state in reversed(path):
                    print(state)
                    print
                print("Goal State is achieved \n \n ")
                print ('Depth is ' + str(len(path)))
                print ('Time taken is ' + str(end - start) +' seconds' )
                break
            # If it is not goal state, increment the depth
            moves += 1
            #1print(current.possible_moves(moves))
            count = 0
            for state in current.possible_moves(moves):
                if state not in closed:
                    #print(state)
                    count += 1
                    #print('\n')
                    open.add(state)
            closed.add(current)
            #print(count)
            overall_count += count
            #print('Total number of states expanded' + str(overall_count))
        else:
            print('The given puzzle is not solvable')
            # Return the total number of states expanded
        return overall_count


class Node:
    def __init__(self, numbers, moves=0, parent=None):
        self.numbers = numbers
        self.moves = moves
        self.parent = parent
        self.goal = range(1, 9)

    def possible_moves(self, moves):
        i = self.numbers.index(0)
        if i in [3, 4, 5, 6, 7, 8]:
            new_board = self.numbers[:]
            new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
            yield State(new_board, moves, self)
        if i in [1, 2, 4, 5, 7, 8]:
            new_board = self.numbers[:]
            new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
            yield State(new_board, moves, self)
        if i in [0, 1, 3, 4, 6, 7]:
            new_board = self.numbers[:]
            new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
            yield State(new_board, moves, self)
        if i in [0, 1, 2, 3, 4, 5]:
            new_board = self.numbers[:]
            new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
            yield State(new_board, moves, self)

    def score(self):


        #return self.misplaced() + self._g()
        #return self.cost()
        #print('The Manhattan Distance is' + str(self.man_dist()))
        return self.cost() + self.man_dist()

    def uniform_cost(self):
        return self.cost()

    def misplaced(self):
        return sum([1 if self.numbers[i] != self.goal[i] else 0 for i in xrange(8)])


    def man_dist(self):
        goal_state =[1, 2, 3, 4, 5, 6, 7, 8, 0]
        #result = 0
        #for i in xrange(0, 9):
            # if self.board[i] != goal[i]:
            #    result += 1
            #n = self.numbers.index(i)
            #m = goal_state.index(i)
            #result += abs((n - m) / 3) + abs(((n / 3) % 3) - ((m / 3) % 3))
        return sum(abs(a-b) for a,b in zip(self.numbers,goal_state))
            #print('Manhattan distance is' + str(result))
            #return result






    def cost(self):
        return self.moves

    def __cmp__(self, other):
        return self.numbers == other.numbers

    def __eq__(self, other):
        return self.__cmp__(other)

    def __hash__(self):
        return hash(str(self.numbers))

    def __lt__(self, other):
        return self.score() < other.score()

    def __str__(self):
        return '\n'.join([str(self.numbers[:3]),
                          str(self.numbers[3:6]),
                          str(self.numbers[6:9])]).replace('[', '').replace(']', '').replace(',', '').replace('0', '0')


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        heappush(self.queue, item)

    def head(self):
        return heappop(self.queue)

    def retrieve(self):
        return self.queue[0]

    def remove(self, item):
        value = self.queue.remove(item)
        heapify(self.queue)
        return value is not None

    def __len__(self):
        return len(self.queue)


def main():
    #puzzle = range(9)
    print("Welcome to CS205 8 puzzle")
    print("Enter 1 to use a default puzzle")
    print("Enter 2 to specify your own puzzle")
    x = int(input('Select your choice'))

    if x==1:
        print('Select the level of difficulty')
        print('1. Trivial\n2. Very Easy ')
        print('3. Easy\n4. Doable')
        print('5. Oh Boy\n6. Impossible')
        y = int(input(''))
        if y==1:
            print('Your choice is Trivial')
            puzzle = [4, 1, 2, 7, 0, 3, 8, 5, 6]
        elif y==2:
            print('Your choice is Very Easy')
            puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        elif y==3:
            print('Your choice is Easy')
            puzzle = [1, 2, 0, 4, 5, 3, 7, 8, 6]
        elif y==4:
            print('Your choice is Doable')
            puzzle = [0, 1, 2, 4, 5, 3, 7, 8, 6]
        elif y==5:
            print('Your choice is Oh Boy')
            puzzle = [8, 7, 1, 6, 0, 2, 5, 4, 3]
        elif y==6:
            print('The number of inversions are odd')
            print('The problem can not be solved')
            exit(0)
        else:
            print('Wrong choice')
    elif x==2:
        puzzle = []
        i=0
        while len(puzzle) < int(9):
            i+=1
            item = int(input('Enter the values of element %d:'%i))
            puzzle.append(item)
            print(puzzle)
    else :
        print('Invalid choice')
        exit(0)

    print('1. Uniform Cost Search')
    print('2. A Star with Misplaced Tile Heuristic')
    print('3. A Star with Manhattan Distance Heuristic')
    algo = int(input('Select your choice of algorithm'))

    if algo == 1:
        solver = Node(puzzle)
        a = solver.search(1)
    if algo == 2:
        solver = Node(puzzle)
        a = solver.search(2)
    if algo == 3:
        solver = Node(puzzle)
        a = solver.search(3)

    print('Total number of states expanded = ' + str(a))

if __name__ == "__main__":
    main()






