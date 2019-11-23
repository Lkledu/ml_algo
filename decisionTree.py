class Node(object):
    def __init__(self, data, isQuestion, left = None, right = None):
        self.left = None
        self.right = None
        self.data = data
        self.isQuestion = isQuestion
    
    def __repr__(self):
        return ( "Node(id=%s, data=%s, isq=%s, left=%s, right=%s)"
            % (id(self), self.data, self.isQuestion,
               id(self.left), id(self.right)))

root = Node("has wings?", True)

def runTree(curNode):
    #isinstance(curNode, object)
    #isinstance(curNode.right, object)

    if (curNode.data != ""):
        print(curNode)
        if(curNode.isQuestion == True):
            print("\n\t")
            print(curNode.data)
            answer = input("\nEnter your input(1-yes, 0-no):\n")
            if(answer == '1'):
                if(curNode.right is None):
                    curNode.right = Node("", False)
                runTree(curNode.right)
            elif(answer == '0'):
                if(curNode.left is None):
                    curNode.left = Node("", False)
                runTree(curNode.left)
    
        else:
                print("\n\t")
                print(curNode.data)
        
    else:
        print(curNode)
        print("\n\n\tERROR: node isn't a question and not has a label yet.\n\n")
        answer = input("Want to put a question(1) or a label(0)?\n")
        if(answer == '1'):
            question = input("write your question\n")
            
            curNode.data = question
            curNode.isQuestion = True
            
            print(curNode)
            print(root)
        elif(answer == '0'):
            label = input("write your label\n")
            
            curNode.data = label
            curNode.isQuestion = False
            
            print(curNode)
            print(root)
        print("\n\n\trunning the decisionTree again\n\n")
        runTree(root)
        
runTree(root)