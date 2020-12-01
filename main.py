class Node:
    def __init__(self, text, previewChoice=None, next=None, isEndNode = False):
        self.next = []
        self.text = text
        self.previewChoice = previewChoice
        self.isEndNode = isEndNode

    def addNext(self, nextList):
        self.next.extend(nextList)


class Story:
    def __init__(self, name, startNode, welcome, setup=None):
        self.name = name
        self.mainCharacter = ""
        self.setupMethod = setup
        self.welcomeMethod = welcome
        self.currNode = startNode
        self.prevNode = None

    def advanceStory(self, chosenNode):
        self.prevNode = self.currNode
        self.currNode = chosenNode

    def welcome(self):
        self.welcomeMethod(self)
    
    def setup(self):
        self.setupMethod(self)


def gameLoop(story):
    
    story.setup()
    story.welcome()

    while(1):
        if story.currNode.isEndNode:
            break
        print(story.currNode.text)
        
        i=1
        
        for node in story.currNode.next:

            print(i, ": ",node.previewChoice)
            i+=1

        chosenPath = int(input("Choose your action"))
        story.advanceStory(story.currNode.next[chosenPath-1])
    
    print(story.currNode.text)



def welcomeDragon(self):
    self.mainCharacter = input("What's your name?")
    print("Welcome to the dragon story", self.mainCharacter)

def dragonSetup(self):
    begin = Node("You come across a evil dragon")
    node1 = Node("you choose to fight the dragon", "fight the dragon", None, False)
    node2 = Node("you escaped from the dragon", "run from the dragon", None, True)
    node3 = Node("Fireball failed you died", "Use a fireball", isEndNode=True)
    node4 = Node("Lightning killed the dragon you win", "Use a lightning spell", isEndNode=True)
    begin.addNext([node1, node2])
    node1.addNext([node3, node4])

    self.currNode = begin

newStory = Story("test", None,welcome=welcomeDragon,setup=dragonSetup)

gameLoop(newStory)

