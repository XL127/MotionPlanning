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
Xmax = 280
Ymax = 340
ScreenSIZE = [Xmax, Ymax]
#################
window = pygame.display.set_mode(ScreenSIZE)
clock = pygame.time.Clock()
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
    ObsList.append(pygame.Rect((100, 140), (40, 40)))
    ObsList.append(pygame.Rect((180, 60), (40, 80)))
    ObsList.append(pygame.Rect((100, 220), (80, 40)))
    ObsList.append(pygame.Rect((160, 200), (20, 20)))

    for rect in ObsList:
        pygame.draw.rect(window, BLUE, rect)

    pygame.draw.polygon(window, RED, ((120, 220), (160, 220), (140, 240)))
    pygame.draw.rect(window, WHITE, ((140, 160), (20, 60)))
    ObsList.append(pygame.Rect((140, 160), (20, 60)))
    pygame.draw.rect(window, RED, ((250, 90), (10, 20))) #goal rectangle
    pygame.draw.rect(window, WHITE, ((220, 80), (60, 1)))
    ObsList.append(pygame.Rect((220, 60), (60, 15)))
    ###########################################
    pygame.draw.circle(window, RED, (40, 300), 1)
    pygame.draw.circle(window, GREEN, (240, 100), 1)
    ###########################################
    pygame.draw.polygon(window, GREEN, ((240, 100), (260, 80), (260, 120)))
    pygame.draw.polygon(window, RED, ((40, 300), (60, 280), (60, 320)))

    ObsList.append(pygame.Rect((80,120), (20,160)))
    pygame.draw.rect(window, RED, ((80,120), (20,160)))
    ObsList.append(pygame.Rect((100,120),(20,20)))
    pygame.draw.rect(window, RED, ((100,120),(40,20)))
    ObsList.append(pygame.Rect((100,260),(80,20)))
    pygame.draw.rect(window, RED,((100,260),(80,20)))
    ObsList.append(pygame.Rect((100,180),(60,40)))
    pygame.draw.rect(window, RED,((100,180),(60,40)))
    ObsList.append(pygame.Rect((160,40),(20,120)))
    pygame.draw.rect(window, RED,((160,40),(20,120)))
    ObsList.append(pygame.Rect((180,40),(40,20)))
    pygame.draw.rect(window, RED, ((180,40),(40,20)))
    ObsList.append(pygame.Rect((180,140),(40, 20)))
    pygame.draw.rect(window, RED,((180,140),(40, 20)))
############################################################
    pygame.draw.polygon(window, WHITE, ((200,40),(220,40),(220,60)))
    pygame.draw.polygon(window, WHITE, ((220,160),(220,140),(200, 160)))
    pygame.draw.polygon(window, WHITE, ((120,120),(140,140),(140,120)))
    pygame.draw.polygon(window, RED, ((160,180),(180,200),(160,200)))
    pygame.draw.polygon(window, WHITE, ((180,280),(160,280),(180,260)))
    pygame.draw.polygon(window,WHITE , ((100,200),(140,200),(120,220)))
    pygame.draw.polygon(window, WHITE, ((120,200),(140, 200), (140,180)))
##########################################################
def randomGnerator():
    while(True):
        randomNode = (random.randint(0, 280)), (random.randint(0,340))
        #randomNode = random.seed() % 600, random.seed() % 600
        if checkCollision(randomNode)== False:
            return randomNode

##########################################################
def checkCollision(check):
    for i in ObsList:
        if i.collidepoint(check) == True:
            return True
    return False

##############################################################
def calculateDistance(pointOne, pointTwo):
    distance = sqrt((pointOne[0] - pointTwo[0]) * (pointOne[0] - pointTwo[0]) + (pointOne[1] - pointTwo[1]) * (
                    pointOne[1] - pointTwo[1]))
    return distance

######################################################################
def EPSILON(p1,p2):
    if calculateDistance(p1,p2) < 15:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + 15*cos(theta), p1[1] + 15*sin(theta)

#############################################################################
def check_cirle_collision(point):
    check = pygame.Rect((250, 90), (10, 20))
   # pygame.draw.rect(screen, RED, ((250, 90), (10, 20)))
    if check.collidepoint(point):
       #print("QQQQQQQQQQQQQQQQQQQQQQQQQ")
        return True
    else:
        return False

#############################################################################
def RRT(state):
    nodeList = []
    nodeList.append(RRtNode((40,300), None))
    goal = RRtNode((240, 100), None)
    init()
    while(True):
        if state == "Initial":
            check = False
            while(check == False):
                randomNode = randomGnerator()
                parentNode = nodeList[0]

                for node in nodeList:
                    if calculateDistance(node.cur, randomNode) <= calculateDistance(parentNode.cur, randomNode):
                      #  newNode = EPSILON(node.cur,randomNode)
                        if checkCollision( EPSILON(node.cur,randomNode)) == False:
                            parentNode = node
                            check = True

            newNode = EPSILON(parentNode.cur, randomNode)
            nodeList.append(RRtNode(newNode, parentNode))
            pygame.draw.line(window, GREEN, parentNode.cur, newNode, 1)
            pygame.display.update()
            #print("BIUBIU")

            if check_cirle_collision(newNode) == True:
                #print("GVVIVIVIU")
                state = 'FindingThePath'
                goalNode = nodeList[len(nodeList) - 1]

        if state == 'FindingThePath':
            currentNode = goalNode.parent
            cost = 0;
            while currentNode.parent != None:
                print("FindingThePath")
                pygame.draw.line(window, BLACK, currentNode.cur, currentNode.parent.cur, 1)
                cost = calculateDistance(currentNode.cur, currentNode.parent.cur) + cost
                pygame.display.update()
                currentNode = currentNode.parent
            state = "cost"

        if state == "cost":
            print("The cost is  ")
            print(cost/20)

if __name__ == '__main__':
    state = "Initial"
    RRT(state)
