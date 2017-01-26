# Imports
import argparse
import sys

#global constants
HEURISTIC = 1

class Node:
    
    def __init__(self,p,y,x,c,goalNode):
        self.parent = p
        self.xPos = x
        self.yPos = y
        self.cost = c
        self.h_cost = self.calcH(goalNode)
        self.f_cost = 32767

	
    def calcH(self,goalNode):

        return 0;	
		
		
#----------------------------------------------------------------------------
# Create the argument parser.
parser = argparse.ArgumentParser(description="Read in a map and run A* on it.")

# Add arguments to the parser.
parser.add_argument("map", help="Path to the map file.")
parser.add_argument("heuristic", help="Which heuristic to use.", type = int, choices = [1,2,3,4,5,6])

# Parses the arguments.
args = parser.parse_args()

# Set the huristic to use
HEURISTIC = args.heuristic

# Open the file.
with open(args.map, 'r') as f:
    arr = [line.strip('\n').split('\t') for line in f]

#DONT FORGET: arrays are -> arr[y][x]
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if (arr[i][j] == 'S'):
            startNode = Node(None,i,j,1,None)
            arr[i][j] = 1
        elif (arr[i][j] == 'G'):
            goalNode = Node(None,i,j,1,None)
            arr[i][j] = 1
        else:
            if (arr[i][j] != "#"):
                arr[i][j] = int(arr[i][j])

for i in range(0, len(arr)):
    print (arr[i])

#----------------------------------------------------------------------------

#init the open list
openList = [startNode]
closedList = []

def 

