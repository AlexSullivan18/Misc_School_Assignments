#this project is a small section of code used for parseing a tree data structure and doing various things with the information found. Also can edit and initilize the tree

class treeNode:
    def __init__(self, type, value, precedence):
        self.type = type
        self.value = value
        self.precedence = precedence

    parent = None
    lChild = None
    rChild = None


def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    # elif type == "LPAREN":
    #     precedence = precedence + 4
    #     print("yes")
    #     print(precedence)
    # elif type == "RPAREN":
    #     precedence = precedence - 4
    #     print("no")
    #     print(precedence)
    return precedence


def createTreeNodeList(tokSeq):
    treeNodeList = []
    count = 0
    for token in tokSeq:
        if token.value == "(":
            count = 4
        if token.value ==")":
            count=0
        newNode = treeNode(token.type, token.value, getPrecedence(token.type)+count)
        treeNodeList.append(newNode)

    return treeNodeList


def parse(tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    rootNode = findRoot(treeNodeList)

    return rootNode


def parsing(treeNodeList):
    # checks for single expressions
    if treeNodeList.__len__() == 1:
        return treeNodeList
    dummyNode = treeNode("DUMMY", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)

    for index in range(len(treeNodeList)):
        node = treeNodeList[index]

        if node.type == "NUMBER":

            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]

            if rOp.precedence > lOp.precedence:
                # right
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp

            else:
                # left
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp


def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:

        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode


def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        print(rootNode.value, end="")
    else:
        print("(", end="")
        printTree(rootNode.lChild)
        print(rootNode.value, end="")
        printTree(rootNode.rChild)
        print(")", end="")
