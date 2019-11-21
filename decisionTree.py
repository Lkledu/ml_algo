class Node(object):
    data  = ""
    isQuestion = False
    left = None
    right = None

    def __init__(self, data = "", isQuestion = False, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
        self.isQuestion = isQuestion

root = Node("tem asa?", True)

def runTree(curNode):
    if (curNode is not None):
        if(curNode.isQuestion == True):
            print("\n\t")
            print(curNode.data)
            answer = input("\nEnter your input(1-yes, 0-no):\n")
            if(answer == '1'):
                runTree(curNode.right)
            elif(answer == '0'):
                runTree(curNode.left)
    
        else:
                print("\n\t")
                print(curNode.data)
        
    else:
        print("\n###########################\nERROR: node isn't a question and not has a label yet.\n###########################\n")
        answer = input("Want to put a question(1) or a label(0)?\n")
        if(answer == '1'):
            question = input("write your question\n")
            curNode = Node(question, True)
            print(curNode)
            print(root)
        elif(answer == '0'):
            label = input("write your label\n")
            curNode = Node(label, False)
            print(curNode)
            print(root)
        print("\n\nrunning the decisionTree again\n###########################\n")
        runTree(root)
        
runTree(root)