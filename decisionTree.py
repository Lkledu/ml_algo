class Node:
    def __init__(self, data, isQuestion = False):

        self.left = None
        self.right = None
        self.data = data
        self.isQuestion = isQuestion


    def PrintTree(self):
        print(self.data)

root = Node("tem asa?", True)
print("#######")

def runTree(currentNode):
    if (currentNode.right is not None):
        print('foi')
    if (currentNode is not None):
        if(currentNode.isQuestion == True):
            print("\n\t")
            print(currentNode.data)
            answer = input("\nEnter your input(1-yes, 0-no):\n")
            if(answer == '1'):
                runTree(currentNode.right)
            elif(answer == '0'):
                runTree(currentNode.left)
    
        else:
                print("\n\t")
                print(currentNode.data)
        
    else:
        print("\n###########################\nERROR: node isn't a question and not has a label yet.\n###########################\n")
        answer = input("Want to put a question(1) or a label(0)?\n")
        if(answer == '1'):
            question = input("write your question\n")
            currentNode = Node(question, True)
            print(currentNode)
        elif(answer == '0'):
            label = input("write your label\n")
            currentNode = Node(label, False)
        print("\n\nrunning the decisionTree again\n###########################\n")
        runTree(root)
        
runTree(root)