import copy
import bisect
import random
import time

solutionMatrix = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
    ["9", "10", "11", "12"],
    ["13", "14", "15", ""],
]


class TreeNode:
    liveNode = []
    visitedNode = set()
    solution = []
    NodeCreated = []

    def __init__(self, parent, matrix, direction, cost, emptyRow, emptyCol):
        self.parent = parent
        self.matrix = matrix
        self.direction = direction
        self.cost = cost
        self.emptyRow = emptyRow
        self.emptyCol = emptyCol

        stringMatrix = toString(matrix)
        if stringMatrix not in self.visitedNode:
            self.visitedNode.add(stringMatrix)
            bisect.insort_right(self.liveNode, self, key=lambda x: x.cost)
            self.liveNode.append(self)
            if self.NodeCreated == []:
                self.NodeCreated.append(0)
            else:
                self.NodeCreated[0] += 1

    def createNewNode(self):
        self.liveNode.remove(self)
        if self.direction != "up" and self.emptyRow != 3:
            newMatrix = move(self.matrix, "down", self.emptyRow, self.emptyCol)
            newCost = cost(newMatrix)
            self.newNode = TreeNode(
                self, newMatrix, "down", newCost, self.emptyRow + 1, self.emptyCol
            )
        if self.direction != "down" and self.emptyRow != 0:
            newMatrix = move(self.matrix, "up", self.emptyRow, self.emptyCol)
            newCost = cost(newMatrix)
            self.newNode = TreeNode(
                self, newMatrix, "up", newCost, self.emptyRow - 1, self.emptyCol
            )
        if self.direction != "left" and self.emptyCol != 3:
            newMatrix = move(self.matrix, "right", self.emptyRow, self.emptyCol)
            newCost = cost(newMatrix)
            self.newNode = TreeNode(
                self, newMatrix, "right", newCost, self.emptyRow, self.emptyCol + 1
            )
        if self.direction != "right" and self.emptyCol != 0:
            newMatrix = move(self.matrix, "left", self.emptyRow, self.emptyCol)
            newCost = cost(newMatrix)
            self.newNode = TreeNode(
                self, newMatrix, "left", newCost, self.emptyRow, self.emptyCol - 1
            )

    def solve(self):
        while cost(self.liveNode[0].matrix) > 0:
            self.liveNode[0].createNewNode()

    def getSolution(self):
        current = self
        while current != None:
            current.solution.append(current)
            current = current.parent

    def printSolution(self):
        for i in range(len(self.solution)):
            print(self.solution[i].direction)
            for j in range (4):
                print(self.solution[i].matrix[j])


# read matrix from txt file
def readMatrix(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        matrix = []
        for line in lines:
            matrix.append(line.split(" "))
    return matrix


# convert matrix to string format
def toString(matrix):
    str = ""
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == "":
                str += " "
            else:
                str += matrix[i][j]
    return str


# get matrix index
def getIndex(element, matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == element:
                return (i, j)
    return (-1, -1)


# compare position of two element, return true if i > j
def comparePosition(i, j, matrix):
    rowI, colI = getIndex(i, matrix)
    rowJ, colJ = getIndex(j, matrix)
    if int(rowI) > int(rowJ):
        return True
    elif int(rowI) == int(rowJ) and int(colI) > int(colJ):
        return True
    else:
        return False


# return value of Kurang(i)
def kurang(i, matrix):
    count = 0
    if i == "16":
        rowI, colI = getIndex("", matrix)
    else:
        rowI, colI = getIndex(i, matrix)

    for row in range(rowI, 4):
        for col in range((colI if row == rowI else 0), 4):
            if matrix[row][col] == "":
                if (int(16) < int(i)) and comparePosition("", i, matrix):
                    count += 1
            else:
                if int(matrix[row][col]) < int(i) and comparePosition(
                    matrix[row][col], i, matrix
                ):
                    count += 1
    return count


# return true if puzzle is solvable
def isSolvable(matrix):
    total = 0
    for i in range(1, 17):
        total += kurang(str(i), matrix)

    rowEmpty, colEmpty = getIndex("", matrix)
    if (rowEmpty + colEmpty) % 2 == 1:
        total += 1
    return total % 2 == 0


# return sum of kurang(i) from 1 to 16
def sumKurang(matrix):
    total = 0
    for i in range(1, 17):
        total += kurang(str(i), matrix)

    rowEmpty, colEmpty = getIndex("", matrix)
    if (rowEmpty + colEmpty) % 2 == 1:
        total += 1
    return total


# return the cost function of the puzzle
def cost(matrix):
    cost = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != solutionMatrix[i][j]:
                cost += 1
    return cost


# move the empty space of the puzzle
def move(matrix, direction, emptyRow, emptyCol):
    newMatrix = copy.deepcopy(matrix)
    if direction == "up":
        newMatrix[emptyRow][emptyCol] = matrix[emptyRow - 1][emptyCol]
        newMatrix[emptyRow - 1][emptyCol] = ""
    elif direction == "down":
        newMatrix[emptyRow][emptyCol] = matrix[emptyRow + 1][emptyCol]
        newMatrix[emptyRow + 1][emptyCol] = ""
    elif direction == "left":
        newMatrix[emptyRow][emptyCol] = matrix[emptyRow][emptyCol - 1]
        newMatrix[emptyRow][emptyCol - 1] = ""
    elif direction == "right":
        newMatrix[emptyRow][emptyCol] = matrix[emptyRow][emptyCol + 1]
        newMatrix[emptyRow][emptyCol + 1] = ""
    return newMatrix


# Create random matrix
def randomizeMatrix():
    elements = [
        "",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]
    random.shuffle(elements)
    matrix = []
    for i in range(4):
        matrix.append([])
        for j in range(4):
            matrix[i].append(elements[i * 4 + j])
    return matrix


# Uncomment code below to run in console

# filename = input("Enter file name: ")
# matrix = readMatrix(filename)
# if isSolvable(matrix):
#     emptyRow, emptyCol = getIndex("", matrix)
#     root = TreeNode(None, matrix, "Start state", cost(matrix), emptyRow, emptyCol)
#     startTime = time.time()
#     root.solve()
#     endTime = time.time()
#     runtime = endTime - startTime
#     root.liveNode[0].getSolution()
#     root.solution.reverse()
#     root.liveNode[0].printSolution()
#     print("Runtime: ", runtime)
#     print("Number of steps: " + str(len(root.solution) - 1))
#     print("Node Created: " + str(root.NodeCreated[0]))
# else:
#     print("Puzzle is not solvable")
