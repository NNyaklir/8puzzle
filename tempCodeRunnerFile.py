def swap_positions(arr2d, pair1, pair2):
    temp=arr2d[pair1.val1,pair1.val2]
    arr2d[pair1.val1,pair2.val2]=arr2d[pair2.val1,pair2.val2]
    arr2d[pair2.val1,pair2.val2]=temp
    return arr2d

#Given the position of '0' and a direction 0, 1, 2, or 3 identify if valid move, and swap.
def move(node, direction):

    node_copy = node.copy
    i = np.argwhere(node_copy==0)
    iPair=Pair(i[0],i[1])

    if direction == 0 and comparePair(iPair,Pair(0,0))==False and comparePair(iPair,Pair(0,1))==False and comparePair(iPair,Pair(0,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0]-1),i[1])
    if direction == 1 and comparePair(iPair,Pair(0,2))==False and comparePair(iPair,Pair(1,2))==False and comparePair(iPair,Pair(2,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0],i[1]+1))
    if direction == 2 and comparePair(iPair,Pair(2,0))==False and comparePair(iPair,Pair(2,1))==False and comparePair(iPair,Pair(2,2))==False:
        return swap_positions(node_copy, iPair, Pair(i[0]+1,i[1]))
    if direction == 3 and comparePair(iPair,Pair(0,0))==False and comparePair(iPair,Pair(1,0))==False and comparePair(iPair,Pair(2,0))==False:
        return swap_positions(node_copy, iPair, Pair(i[0],i[1]-1))

    return node.copy()