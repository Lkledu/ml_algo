class Node:
    def __init__(self, data, isQuestion = None):

        self.left = None
        self.right = None
        self.data = data
        self.isQuestion = isQuestion


    def PrintTree(self):
        print(self.data)

root = Node("tem asa?", True)
print("#######")

def runTree(currentNode):
    if (currentNode is not None):
        if(currentNode.isQuestion == True):
            print("\n")
            print(currentNode.data)
            answer = input('\nEnter your input(1-yes, 0-no):\n')
            if(answer == 1):
                runTree(currentNode.right)
            else:
                runTree(currentNode.left)
    
        else:
                print("\n")
                print(currentNode.data)
        
    else:
        print("\n\tERROR: node isn't a question and not has a label yet.\n\n")
        answer = input("Want to put a question(1) or a label(0)?\n")
        if(answer == 1):
            question = input("write your question")
            currentNode = Node(question, True)
        else:
            label = input("write your label")
            currentNode = Node(label, False)
        print("we'll run the decisionTree again")
        runTree(root)
        
runTree(root)