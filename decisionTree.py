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
print(type(root.left.data))
print("&&&&&")
print(root.left.data)

def runTree(currentNode):
    if currentNode.data is not None:
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
        
runTree(root)