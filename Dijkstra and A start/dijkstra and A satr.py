#This is the implmentation of dijkstra and A* algorithm

from math import sqrt

#################################################################################
#This function is for calculating the heuristics from a a vertext to the goalVertext
#################################################################################
def heuristics(vertices, goalX, goalY):
    currentX, currentY = data[vertices]
    currentX = float(currentX)
    currentY = float(currentY)
    return sqrt((currentX - goalX) * (currentX - goalX) + (currentY - goalY) * (currentY - goalY))


if __name__=='__main__':

##############################################################################
#This section of code read in all the cost information into a 2D array called verticesInfo
#and read all the coordinates information into a list called data
##############################################################################

    inputList = ["input_1.txt", "input_2.txt", "input_3.txt"]  
    coordsList = ["coords_1.txt", "coords_2.txt", "coords_3.txt"] #stores all the coordinates of all point

    i = 0
    totalVertex = 0
    startVertex = 0
    endVertex = 0

    out_cost = open("output_costs.txt", 'w')
    out_iteration = open("output_numiters.txt", 'w')
    for i in range(len(inputList)):
        inputFile = inputList[i]
        coordsFile = coordsList[i]
        txt_File = open(inputFile, 'r')
        coords_File = open(coordsFile, 'r')

        data = []
        i = 0
        for coords in coords_File: #this for loop puts all the coords information into data list
            tempCoords = coords.rstrip('\n').split(" ")
            data.append((tempCoords[0], tempCoords[1]))  

        for test in txt_File:
            if (i == 0):
                totalVertex = int(test)
                verticesInfo = [[0 for x in range(totalVertex)] for x in range(totalVertex)]
            if (i == 1):
                startVertex = int(test)
            if (i == 2):
                endVertex = int(test)
            if (i > 2):
                temp = test.rstrip('\n').split(" ")
                temp[0] = int(temp[0])
                temp[1] = int(temp[1])
                temp[2] = float(temp[2])
                verticesInfo[temp[0] - 1][temp[1] - 1] = temp[2]
            i = i + 1

        goalX, goalY = data[endVertex - 1]
        goalX = float(goalX)
        goalY = float(goalY) #find the endvertex coordinates information

		
		
        for Iterator in range(2): #if Iterator is 0 then this is a dijkstra, if it is 1 then this is A star
		
		
######################################################################################################
#Create three lists, which are closelist, openlist and valuelist 
#openlist is the univisted list and closelist is the visisted list and valuelist stores the least cost
#from the start of all the vertex in close list
#####################################################################################################

            closeList = []
            openList = []
            valueList = []
            openList.append(startVertex - 1)
            for j in range(totalVertex):
                if (j == startVertex - 1):
                    valueList.append(0)
                else:
                    valueList.append(float("inf"))
					
            minCostForOpenList = float("inf") #store the minCost in openlist and the corrsponding index
            minCostIndex = -1
			
			
############################################################################################
#The following part is the main algorithm
#############################################################################################
			
            while (1):
                minCostForOpenList = float("inf")
                minCostIndex = -1                    #reset those two varible every loop
                if endVertex - 1 in closeList:
                    break                            #if endVertex is in the close list, then end the loop

                for i in range(len(openList)):
                    if (valueList[openList[i]] + heuristics(openList[i], goalX, goalY) * Iterator < minCostForOpenList):
                        minCostForOpenList = valueList[openList[i]] + heuristics(openList[i], goalX, goalY) * Iterator
                        minCostIndex = openList[i]
                #################find the vertex has the min cost to startVertex in the openlist and update the minCostForOpenList and minCostIndex
				

                for i in range(len(verticesInfo[minCostIndex])):
                    if (verticesInfo[minCostIndex][i] != 0):
                        if (i not in closeList and i not in openList):
                            openList.append(i)
                ################put all neighbors of new minIndex in openList
				

                closeList.append(minCostIndex)
                openList.remove(minCostIndex)
                ###############delet minCostIndex from openlist and append in close list
				
				

                for i in range(len(openList)):
                    if (verticesInfo[minCostIndex][openList[i]] != 0):
                        costNew = valueList[minCostIndex] + verticesInfo[minCostIndex][openList[i]]
                        if (costNew < valueList[openList[i]]):
                            valueList[openList[i]] = costNew       
				############################ update the valuelist if the cost from the new minCostIndex to opanlist[i] is smaller than the old one(update[openlist[i])
				
				
            out_cost.write(str(valueList[endVertex - 1]))
            out_cost.write("  ")
            out_iteration.write(str(len(closeList)))
            out_iteration.write("  ")

        out_cost.write('\n')
        out_iteration.write('\n')




