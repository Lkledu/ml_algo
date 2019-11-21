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
            answer = input('Enter your input(1-yes, 0-no):')
            if(answer == 1):
                runTree(currentNode.right)
            else:
                runTree(currentNode.left)
    
        else:
                print("\n")
                print(currentNode.data)
        
    else:
        print("ERROR: node isn't a question and not has a label yet.")
        answer =input("Want to put a question(1) or a label(0)?")
        if(answer == 1){
            currentNode.isQuestion = True
            currentNode.data = input("write your question")
        }else{
            currentNode.isQuestion = False
            currentNode.data = input("write your label")
        }
        print("we'll run the decisionTree again")
        runTree(root)
        
runTree(root)