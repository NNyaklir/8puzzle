#<Devin Gill> <88747939> CS4390

#!/usr/bin/env python3
import os
import ast
import numpy as np

class Pair: #class to store two values
    def __init__(self,val1,val2):
        self.val1= val1
        self.val2= val2
        
def comparePair(p1,p2): #function to compare two pairs
    if p1.val1==p2.val1 and p1.val2==p2.val2:
        return True
    else:
        return False
    

#Reverse the given list. 
def reverse_list(lst):
    return list(reversed(lst))

#Swap the elements of 2darray in position 1 and position 2.
def swap_positions(arr2d, pair1, pair2):
    temp=arr2d[pair1.val1,pair1.val2]
    arr2d[pair1.val1,pair1.val2]=arr2d[pair2.val1,pair2.val2]
    arr2d[pair2.val1,pair2.val2]=temp
    return arr2d

#Given the position of '0' and a direction 0, 1, 2, or 3 identify if valid move, and swap.
def move(node, direction):

    node_copy = node.copy()
    #print(node_copy)
    i = np.argwhere(node_copy==0)[0]
    #print(i)
    iPair=Pair(i[0],i[1])
    #print(iPair.val1,iPair.val2)

    if direction == 0 and comparePair(iPair,Pair(0,0))==False and comparePair(iPair,Pair(0,1))==False and comparePair(iPair,Pair(0,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0]-1,i[1]))
    if direction == 1 and comparePair(iPair,Pair(0,2))==False and comparePair(iPair,Pair(1,2))==False and comparePair(iPair,Pair(2,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0],i[1]+1))
    if direction == 2 and comparePair(iPair,Pair(2,0))==False and comparePair(iPair,Pair(2,1))==False and comparePair(iPair,Pair(2,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0]+1,i[1]))
    if direction == 3 and comparePair(iPair,Pair(0,0))==False and comparePair(iPair,Pair(1,0))==False and comparePair(iPair,Pair(2,0))==False:
        return swap_positions(node_copy, iPair, Pair(i[0],i[1]-1))

    return node.copy()

#Given the visited and parents, backtrack path to origin.
def generate_path(index, visited, parents):
    print("Backtracking------------")
    path = [(visited[-1])]
    while index != 0:
        node = (visited[index])
        path.append(node)
        index = parents[index]
    path.append(visited[0])
    return reverse_list(path)

def arrIn(lst,arr2d):
    for i in lst:
        if (arr2d==i).sum()==9:
            return True
    return False

def arrInd(lst,arr2d):
    for i in range (len(lst)):
        if (arr2d==lst[i]).sum()==9:
            return i
    return -1

#Brute force path to all 4 directions, and append visited to set.
def bfs(data, goal, visited):
    print("Running----------------")
    parent_i = [0]
    #while not arrIn(data,goal):
    while len(data)>0:
        
        node = data.pop(0)
        for d in range(4):
            if not arrIn(visited,goal):
                test = move(node, d).copy()
                if not arrIn(visited,test):
                    parent_i.append(arrInd(visited,node))
                    visited.append(test)
                    data.append(test)
    else:
        print("Goal Reached !!!")
    return parent_i
                    
        
    

#Main method, start state, run BFS, and create reference files.
def run(start, goal):
    location = os.getcwd() + "/"
    node_i = np.array(start)
    node_goal = np.array(goal)
    data = [node_i]
    visited = [node_i]
    parents = bfs(data, node_goal, visited)
    index = parents[-1]
    path = generate_path(index, visited, parents)

    with open(location + "nodePath.txt", "w") as textfile:
        print("Writing Path File")
        for element in path:
            textfile.write(" ".join(map(str, element)) + "\n")

    with open(location + "NodesInfo.txt", "w") as textfile:
        print("Writing Node Info")
        textfile.write("Node_index  Parent_index  cost\n")
        for i, _ in enumerate(visited):
            textfile.write(f"{i}             {parents[i]}              0\n")

    print("All Done!")

    with open(location + "Nodes.txt", "w") as textfile:
        print("Writing Node File")
        for element in visited:
            temp = element
            textfile.write(" ".join(map(str, temp)) + "\n")

# Change these start and goal nodes
##############
node_start = [1, 5, 0], [2, 4, 3], [7, 8, 6]
node_goal1 = [1, 2, 3], [4, 5, 6], [7, 8, 0]

##############

run(node_start,node_goal1)
