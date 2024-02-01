#student ID here

#should use a 2d array for the initial and final state.
#use hash set for storing unique boards?
import array as arr

#2d arrays
boardInitial= [1, 5, 0], [2, 4, 3], [7, 8, 6]

boradFinal = [1, 2, 3], [4, 5, 6], [7, 8, 0]

class Pair: #class to store two values
    def __init__(self,val1,val2):
        self.val1= val1
        self.val2= val2
        
def comparePair(p1,p2): #function to compare two pairs
    if p1.val1==p2.val1 and p1.val2==p2.val2:
        return True
    else:
        return False
    
def validMove (pos1,pos2): #checks if a move from one position to another is valid
    #valid moves are for [0->1,0->3],[1->0,1->2,1->4]
    #[2->1,2->5]  [3->0,3->4,3->6]
    #[4->1,4->3,4->5,4->7]
    #[5->2,5->4,5->8]
    #[6->3,6-7]  [7->6,7->4,7->8]
    #[8->7,8->5]
    validMoves = arr.array (i,[Pair(0,1),Pair(0,3),Pair(1,0),Pair(1,2),Pair(1,4),
                               Pair(2,1),Pair(2,5),Pair(3,0),Pair(3,4),Pair(3,6),
                               Pair(4,1),Pair(4,3),Pair(4,5),Pair(4,7),Pair(5,2),
                               Pair(5,4),Pair(5,8),Pair(6,3),Pair(6,7),Pair(7,6),
                               Pair(7,4),Pair(7,8),Pair(8,7),Pair(8,5)])
    consideredMove=Pair(pos1,pos2)
    check=False
    for i in validMoves:
        if comparePair(validMoves[i],consideredMove)==True:
            check=True
            
    return check
        
    """This is the position table
        [(00)=0,(01)=1,(02)=2
         (10)=3,(11)=4,(12)=5
         (20)=6,(21)=7,(22)=8]
    """
def valueCoordX(arr2d,value): #finds x value of number in array
    for i in range(len(arr2d)):
        for j in range(len(arr2d[i])):
            if arr2d[i,j]==value:
                return i
            
def valueCoordY(arr2d,value): #finds y value of number in array
    for i in range(len(arr2d)):
        for j in range(len(arr2d[i])):
            if arr2d[i,j]==value:
                return j
            
            
def findPosition(arr2d,number): #finds position of the number in the array
    for i in range(len(arr2d)):
        for j in range(len(arr2d[i])):
            if arr2d[i,j]==number:
                if i==0 and j==0: return 0
                elif i==0 and j==1: return 1
                elif i==0 and j==2: return 2
                elif i==1 and j==0: return 3
                elif i==1 and j==1: return 2
                elif i==1 and j==2: return 2
                elif i==2 and j==0: return 2
                elif i==2 and j==1: return 2
                elif i==2 and j==2: return 2
    
            
def swapPos (arr2d, number1, number2): #swaps two positions of numbers in the array by finding their position, finding the coordinates
    pos1= findPosition(arr2d,number1)  # and then finally replacing values
    pos2= findPosition(arr2d,number2)
    if validMove(pos1,pos2):
        pos1X= valueCoordX(arr2d,number1)
        pos1Y= valueCoordY(arr2d,number1)
        pos2X= valueCoordX(arr2d,number2)
        pos2Y= valueCoordY(arr2d,number2)
        arr2d[pos2X,pos2Y]=number2
        arr2d[pos1X,pos1Y]=number1