import time
import Puzzle15
from tkinter import *
import threading


# get input from textBox
def getInput():
    global inputValue
    global puzzleMatrix
    inputValue = textBox.get("1.0", "end-1c")
    puzzleMatrix = Puzzle15.readMatrix(inputValue)
    setPuzzle(puzzleCell, puzzleMatrix)
    if Puzzle15.isSolvable(puzzleMatrix):
        Label(root, text="--Solvable--", fg="green").grid(row=1, column=0)
    else:
        Label(root, text="Not Solvable", fg="red").grid(row=1, column=0)
    showKurang()


# generate random puzzle Matrix
def randomize():
    global puzzleMatrix
    puzzleMatrix = Puzzle15.randomizeMatrix()
    setPuzzle(puzzleCell, puzzleMatrix)
    if Puzzle15.isSolvable(puzzleMatrix):
        Label(root, text="--Solvable--", fg="green").grid(row=1, column=0)
    else:
        Label(root, text="Not Solvable", fg="red").grid(row=1, column=0)
    showKurang()


# set Puzzle Frame
def setPuzzle(puzzleCell, Matrix):
    for i in range(4):
        for j in range(4):
            if Matrix[i][j] == "":
                puzzleCell[i][j].config(text="", bg="white")
            else:
                puzzleCell[i][j].config(text=Matrix[i][j], bg="lightblue")


def showKurang():
    for i in range(1, 17):
        Label(
            rightFrame,
            text="Kurang("
            + str(i)
            + ") = "
            + str(Puzzle15.kurang(str(i), puzzleMatrix)),
        ).grid(row=i, column=0)

        Label(
            rightFrame,
            text="SUM(Kurang(i)) + X = " + str(Puzzle15.sumKurang(puzzleMatrix)),
        ).grid(row=17, column=0)


# solve puzzle and show solution animation
def showSolution():
    global puzzleMatrix
    emptyRow, emptyCol = Puzzle15.getIndex("", puzzleMatrix)
    tree = Puzzle15.TreeNode(
        None,
        puzzleMatrix,
        "start state",
        Puzzle15.cost(puzzleMatrix),
        emptyRow,
        emptyCol,
    )

    if Puzzle15.isSolvable(puzzleMatrix):
        Label(root, text="Loading solution", fg="blue").grid(row=3, column=0)
        startTime = time.time()
        tree.solve()
        endTime = time.time()
        runTime = endTime - startTime

        tree.liveNode[0].getSolution()
        tree.liveNode[0].solution.reverse()

        Label(root, text="Run time: " + ("%.5f" % runTime)).grid(row=3, column=0)
        steps = len(tree.solution) - 1
        Label(root, text="Number of steps: " + str("%3.f" % steps)).grid(
            row=4, column=0
        )
        Label(root, text="---Node Created: " + str(tree.NodeCreated[0]) + "---").grid(
            row=5, column=0
        )
        Label(
            root, text="List of steps is printed in the console!", bg="lightgreen"
        ).grid(row=6, column=0)

        print("==============")
        print("=  Solution  =")
        print("==============")
        for i in range(len(tree.solution)):
            time.sleep(0.05)
            setPuzzle(puzzleCell, tree.solution[i].matrix)
            print(tree.solution[i].direction)
            for j in range(4):
                print(tree.solution[i].matrix[j])
            # print(tree.solution[i].matrix)

    del tree.solution[:]
    del tree.liveNode[:]
    tree.visitedNode.clear()
    del tree.NodeCreated[:]


# return solution step by step
def threadingShowSolution():
    t = threading.Thread(target=showSolution)
    t.start()


root = Tk()
root.title("15 Puzzle Solver")
puzzleFrame = Frame(root)
puzzleFrame.grid(row=0, column=0, padx=10, pady=10)
rightFrame = Frame(root)
rightFrame.grid(row=0, column=1, padx=10, pady=10)


# make a 2d array containing puzzle border
puzzleCell = []
for i in range(4):
    puzzleCell.append([])
    for j in range(4):
        puzzleCell[i].append(
            Label(puzzleFrame, borderwidth=4, width=8, height=4, relief="raised")
        )
        puzzleCell[i][j].grid(row=i, column=j)


Label(puzzleFrame, text="Input filename:").grid(row=0, column=4)
textBox = Text(puzzleFrame, height=1, width=20)
textBox.grid(row=1, column=4, padx=10, pady=10)

submitButton = Button(
    puzzleFrame,
    text="Submit",
    command=lambda: getInput(),
    padx=5,
    pady=5,
    bg="lightyellow",
    borderwidth=4,
)
submitButton.grid(row=1, column=5, padx=10, pady=10)

randomizeButton = Button(
    puzzleFrame,
    text="Randomize",
    command=lambda: randomize(),
    padx=10,
    pady=10,
    bg="lightblue",
    borderwidth=4,
)
randomizeButton.grid(row=2, column=4, padx=10, pady=10)

solveButton = Button(
    root,
    text="Solve",
    command=threadingShowSolution,
    padx=10,
    pady=10,
    bg="yellow",
    borderwidth=4,
)
solveButton.grid(row=2, column=0, padx=5, pady=5)


root.mainloop()
