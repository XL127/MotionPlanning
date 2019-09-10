import sys, random, math, pygame
from pygame.locals import *
from math import sqrt,cos,sin,atan2

pygame.init()
################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
################
Xmax = 600
Ymax = 600
ScreenSIZE = [Xmax, Ymax]
#################
window = pygame.display.set_mode(ScreenSIZE)
#clock = pygame.time.Clock()
################
ObsList = []

########################################################
class RRtNode():
    def __init__(self, cur, parent):
        self.cur = cur
        self.parent = parent
#######################################################

def init():
    window.fill(WHITE)
    ObsList.append(pygame.Rect((100, 100), (20, 400)))
    ObsList.append(pygame.Rect((100, 480), (400, 20)))
    ObsList.append(pygame.Rect((480, 100), (20, 400)))
    ObsList.append(pygame.Rect((140, 100), (360, 20)))
    ObsList.append(pygame.Rect((140, 140), (20, 320)))
    ObsList.append(pygame.Rect((140, 440), (300, 20)))
    ObsList.append(pygame.Rect((420, 140), (20, 140)))
    ObsList.append(pygame.Rect((420, 300), (20, 140)))
    ObsList.append(pygame.Rect((140, 140), (300, 20)))
    ObsList.append(pygame.Rect((200, 200), (20, 80)))
    ObsList.append(pygame.Rect((200, 300), (20, 100)))
    ObsList.append(pygame.Rect((200, 380), (180, 20)))
    ObsList.append(pygame.Rect((360, 200), (20, 200)))
    ObsList.append(pygame.Rect((200, 200), (180, 20)))
    ObsList.append(pygame.Rect((240, 240), (20, 100)))
    ObsList.append(pygame.Rect((320, 240), (20, 100)))
    ObsList.append(pygame.Rect((240, 240), (40, 20)))
    ObsList.append(pygame.Rect((240, 340), (40, 20)))
    ObsList.append(pygame.Rect((300, 240), (40, 20)))
    ObsList.append(pygame.Rect((300, 340), (40, 20)))

    for rect in ObsList:
        pygame.draw.rect(window, BLUE, rect)

    pygame.draw.circle(window, RED, (300, 300), 10)
    pygame.draw.circle(window, GREEN, (540, 60), 10)

##########################################################
def randomGnerator():
    while(True):
        randomNode = (random.randint(0, 600)), (random.randint(0,600))
        if checkCollision(randomNode)== False:
            return randomNode

##########################################################
def checkCollision(check):
    for i in ObsList:
        if i.collidepoint(check) == True:
            return True
    return False

##############################################################
def calculateDistance(pointOne,pointTwo):
        distance = sqrt((pointOne[0] - pointTwo[0]) * (pointOne[0] - pointTwo[0]) + (pointOne[1] - pointTwo[1]) * (pointOne[1] - pointTwo[1]))
        return distance

######################################################################
def EPSILON(p1,p2):
    if calculateDistance(p1,p2) < 20:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + 20*cos(theta), p1[1] + 20*sin(theta)

#############################################################################
def check_cirle_collision(point1, point2, radius):
    if calculateDistance(point1,point2) < radius:
        return True
    else:
        return False

#############################################################################
def RRT(state):
    nodeList = []
    nodeList.append(RRtNode((300,300), None))
    goal = RRtNode((540, 60), None)
    init()
    while(True):
        if state == "Initial":
            check = False
            while(check == False):
                randomNode = randomGnerator()
                parentNode = nodeList[0]
                for node in nodeList:
                    if calculateDistance(node.cur, randomNode) <= calculateDistance(parentNode.cur, randomNode):
                        newNode = EPSILON(node.cur,randomNode)
                        if checkCollision(newNode) == False:
                            parentNode = node
                            check = True

            newNode = EPSILON(parentNode.cur, randomNode)
            nodeList.append(RRtNode(newNode, parentNode))
            pygame.draw.line(window, GREEN, parentNode.cur, newNode, 1)
            pygame.display.update()
            #print("BIUBIU")

            if check_cirle_collision(newNode, goal.cur, 10) == True:
                #print("GVVIVIVIU")
                state = 'FindingThePath'
                goalNode = nodeList[len(nodeList) - 1]

        if state == 'FindingThePath':
            currentNode = goalNode.parent
            cost = 0;
            while currentNode.parent != None:
                print("FindingThePath")
                pygame.draw.line(window, BLACK,currentNode.cur,currentNode.parent.cur,1)
                cost = cost + calculateDistance(currentNode.cur,currentNode.parent.cur)
                pygame.display.update()
                currentNode = currentNode.parent
            state = "Finish"

        if state == "Finish":
            print ("The cost is   ")
            print (cost/20)


if __name__ == '__main__':
    state = "Initial"
    RRT(state)
