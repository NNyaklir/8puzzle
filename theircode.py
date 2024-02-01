#<Student Name> <Student ID> CS4390

#!/usr/bin/env python3
import os
import ast
import numpy as np

#Reverse the given list.
def reverse_list(lst):
    return list(reversed(lst))

#Transform 2D array grid into a 1D array and then into a list.
def reshape_array(node):
    return np.reshape(np.array(node), 9).tolist()

#Swap the elements of list in position 1 and position 2.
def swap_positions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

#Given the position of '0' and a direction 0, 1, 2, or 3 identify if valid move, and swap.
def move(node, direction):
    node_copy = node.copy()
    i = node_copy.index(0)

    if direction == 3 and i not in [0, 1, 2]:
        return swap_positions(node_copy, i, i - 3)
    if direction == 2 and i not in [2, 5, 8]:
        return swap_positions(node_copy, i, i + 1)
    if direction == 1 and i not in [6, 7, 8]:
        return swap_positions(node_copy, i, i + 3)
    if direction == 0 and i not in [0, 3, 6]:
        return swap_positions(node_copy, i, i - 1)

    return node.copy()

#Given the visited and parents, backtrack path to origin.
def generate_path(index, visited, parents):
    print("Backtracking------------")
    path = [ast.literal_eval(visited[-1])]
    while index != 0:
        node = ast.literal_eval(visited[index])
        path.append(node)
        index = parents[index]
    path.append(ast.literal_eval(visited[0]))
    return reverse_list(path)

#Brute force path to all 4 directions, and append visited to set.
def bfs(data, goal, visited):
    print("Running----------------")
    parent_i = [0]
    while str(goal) not in data:
        node = data.pop(0)
        node_i = ast.literal_eval(node)
        for d in range(4):
            if str(goal) not in visited:
                test = move(node_i, d).copy()
                if str(test) not in visited:
                    parent_i.append(visited.index(node))
                    visited.append(str(test))
                    data.append(str(test))
    else:
        print("Goal Reached !!!")
    return parent_i

#Main method, start state, run BFS, and create reference files.
def run(start, goal):
    location = os.getcwd() + "/"
    node_i = reshape_array(start)
    node_goal = reshape_array(goal)
    data = [str(node_i)]
    visited = [str(node_i)]
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
            temp = ast.literal_eval(element)
            textfile.write(" ".join(map(str, temp)) + "\n")

# Change these start and goal nodes
##############
node_start = [1, 5, 0], [2, 4, 3], [7, 8, 6]
node_goal1 = [1, 2, 3], [4, 5, 6], [7, 8, 0]

##############

run(node_start,node_goal1)
