file = open("input.txt", 'r')
i = 0
totalVertex = 0
startVertex = 0
endVertex = 0
output= open("output.txt", 'w')
for test in  file:
    if(i == 0):
        totalVertex = int(test)
        verticesInfo = [[0 for x in range(totalVertex)] for x in range(totalVertex)]
    if(i == 1):
        startVertex= int(test)
    if(i == 2):
        endVertex = int(test)
    if(i > 2):
        temp = test.rstrip('\n').split(" ")
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        temp[2] = float(temp[2])
        verticesInfo[temp[1]-1][temp[0]-1] = temp[2]
    i = i + 1

################################################################
table = []
for index in range(totalVertex):
   table.append(float('inf'))

table[endVertex-1] = 0

#################################################################

for k in range(totalVertex -1):
    #sprint(table)
    for i in range(totalVertex):
        if(table[i] != float('inf')):
            #print(table[i])
            for j in range(len(verticesInfo[i])):
              #  print(verticesInfo[i])
                if(verticesInfo[i][j] != 0):
                    if(verticesInfo[i][j] + table[i] < table[j]):
                        table[j] = verticesInfo[i][j] + table[i]
#################################################################
file = open("input.txt", 'r')
pathHelperTable = [[0 for y in range(totalVertex)] for y in range(totalVertex)]
count = 0
for test in  file:
    if (count > 2):
        temp = test.rstrip('\n').split(" ")
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        temp[2] = float(temp[2])
        pathHelperTable[temp[0] - 1][temp[1] - 1] = temp[2]
    count = count + 1

pathSearchPointer = startVertex-1
minCost = float('inf')
minVertex= 0
minVertexArray = []
minVertexArray.append(pathSearchPointer)
while(1):
    if(pathSearchPointer == endVertex-1):
        break
    for increment in range(len(pathHelperTable[pathSearchPointer])):
        if(pathHelperTable[pathSearchPointer][increment] != 0):
            #print(pathHelperTable[increment])
            if(table[increment] + pathHelperTable[pathSearchPointer][increment] < minCost):
                minCost = table[increment] + pathHelperTable[pathSearchPointer][increment]
                minVertex = increment
    pathSearchPointer = minVertex
    minVertexArray.append(pathSearchPointer)

for counter in range(len(minVertexArray)):
    minVertexArray[counter] = minVertexArray[counter] + 1

print(minVertexArray)
print(table)
output.write(str(minVertexArray))
output.write('\n')
output.write(str(table))
#######################################################################################