class Node:
    def __init__(self, wRemaining, level, numBoxes):   
        self.wRemaining = wRemaining    #array of remaining weight for each box 
        self.level = level              #the level of the node in branch and bound tree 
        self.numBoxes = numBoxes        #number of used boxes  

    def getLevel(self):        
        return self.level

    def getNumberBoxes(self):                              
        return self.numBoxes

    def getWRemainings(self):                              
        return self.wRemaining

    def getWRemaining(self, i):                             
        return self.wRemaining[i]


#branch and bound bin packing exact algorithm
def branchAndBound(n, c, w):

    minBoxes = n    #initialize the number of used boxes 
    Nodes = []      #array contains the unprocessed nodes
    wRemaining = [c]*n  #array contains remaining weight in each box [c,c,c,.......c]
    numBoxes = 0    #initialise number of used boxes 

    curN = Node(wRemaining, 0, numBoxes)    #create the root node, level 0, number of used boxes 0

    Nodes.append(curN)  #add the root node to Nodes

    while len(Nodes) > 0 :  #As long as Nodes is not empty do 

        curN = Nodes.pop()      #get a node to process it : curent node (curN)
        curLevel = curN.getLevel()  #get the level of curN

        if (curLevel == n) and (curN.getNumberBoxes() < minBoxes):  #if this node is a leaf of the tree and the number of used boxes < minBoxes
            minBoxes = curN.getNumberBoxes()    #update minBoxes

        else:
            indNewBox = curN.getNumberBoxes()   

            if (indNewBox < minBoxes ):     #else, if from this node the number of used boxes < minBoxes (not dominated)

                wCurLevel = w[curLevel]     
                for i in range(indNewBox+1):    #we will try to add the following item in each box already used, and in a new box (that's why I added +1 to indNewBox)
                        
                    if  (curLevel < n) and (curN.getWRemaining(i) >= wCurLevel):    #if it is possible to add the item in the box i (weight remaining in the box > weight of the item)
                                                                                    #we will create a node and add it to Nodes.
                        newWRemaining = curN.getWRemainings().copy()
                        newWRemaining[i] -= wCurLevel                       #remaining weight in box i - weight of the item to be added

                        if (i == indNewBox):                                            #new Box 
                            newNode = Node(newWRemaining, curLevel + 1, indNewBox + 1)
                        else:                                                           #already used box
                            newNode = Node(newWRemaining, curLevel + 1, indNewBox)
                        
                        Nodes.append(newNode)
        
    return minBoxes
