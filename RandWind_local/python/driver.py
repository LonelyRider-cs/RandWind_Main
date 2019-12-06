# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:14:29 2019

@author: Adam Salyers
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:55:42 2019

@author: Adam Salyers
"""
import string

class Node(object):

    def __init__(self, label = "", left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

mynums = ["0","1","2","3","4","5","6","7","8","9","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c"]

def createtree(mynums):
   # print("starting function")
    n = len(mynums)
    #print("N is: ", n)
    num1 = 2
    count = [0]
    while n > num1:
        num1 *= 2
        count.append(0)
    mytree = Node()
    my1s = 0
    for i in range(n):
        #print("Iteration: ", i)
        if i == 0:
            myval = "0"
            mytree.left = Node(myval)
            cnode = mytree.left
            for j in range(1, len(count)):
                myval += "0"
                if j == len(count)-1:
                    cnode.left = Node(mynums[i])
                    #print("adding: ", mynums[i])
                    break
                else:
                    #print("Adding node")
                    cnode.left = Node(myval)
                    cnode = cnode.left
        else:
            myval = ""
            cnode = mytree
            for j in reversed(range(len(count))):
                if my1s == len(count):
                        #print("Returning tree")
                        return mytree, len(count)
                if count[j] == 0:
                    count[j] = 1
                    break
                elif count[j] == 1:
                    count[j] = 0
                if j == 0:
                    my1s += 1
            #print ("Count is: ", count)

            for z in range(len(count)):
                if count[z] == 0:
                    myval += "0"
                    #print("going on node: ", myval)
                    if cnode.left == None:
                        if z == len(count)-1:
                            cnode.left = Node(mynums[i])
                            #print("adding: ", mynums[i])
                            break
                        else:
                            cnode.left = Node(myval)
                            cnode = cnode.left
                    else:
                        cnode = cnode.left
                else:
                    myval+="1"
                    #print("going on node: ", myval)
                    if cnode.right == None:
                        if z == len(count)-1:
                            cnode.right = Node(mynums[i])
                            #print("adding: ", mynums[i])
                            break
                        else:
                            cnode.right = Node(myval)
                            cnode = cnode.right
                    else:
                        cnode = cnode.right
    return mytree, len(count)

def printtree(mytree):
    if mytree.left == None and mytree.right == None:
        print(mytree.label)
        return
    if mytree.left != None:
        printtree(mytree.left)
    if mytree.right != None:
        printtree(mytree.right)
    return

def getvalue(mytree, code):
    for i in range(len(code)):
        if code[i] == 0:
            if mytree.left != None:
                mytree = mytree.left
                if i == len(code)-1:
                    return mytree.label
            else:
                return "SKIP"

        if code[i] == 1:
            if mytree.right != None:
                mytree = mytree.right
                if i == len(code)-1:
                    return mytree.label
            else:
                return "SKIP"

def driverFunc(numoptions,numreturns,frame):
    myoutput = []
    #myoutput = ""
    if numoptions == 8:
        mynums = ["0","1","2","3","4","5","6","7"]
        mytree, num = createtree(mynums)
        num01 = 3*numreturns
    elif numoptions == 10:
        mynums = ["0","1","2","3","4","5","6","7","8","9"]
        mytree, num = createtree(mynums)
        num01 = 4*numreturns
    elif numoptions == 16:
        mynums = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        mytree, num = createtree(mynums)
        num01 = 4*numreturns
    else:
        mynums = []
        for i in string.printable:
            mynums.append(i)
            mytree, num = createtree(mynums)
        num01 = 7*numreturns
    #my1s,frame = contourfunc(num01,frame)
    with open("random10.txt", "r") as myfile:
        filecont = myfile.read()
        print("File contents length: ",len(filecont))
        i = 0
        my1s = []
        while i < len(filecont):
            if i == len(filecont):
                print("Breaking")
                break
            if filecont[i] == "0":
                #print("Appending a 0")
                my1s.append(0)
                i += 1
            elif filecont[i] == "1":
                #print("Appending a 1")
                my1s.append(1)
                i += 1
    i = 0
    print("length of my1's is: ",len(my1s))
    while i < len(my1s):
        mycurr = []
        for j in range(num):
            if i == len(my1s):
                print("Breaking")
                break
            mycurr.append(my1s[i])
            i += 1
        if i < len(my1s):
            myoutput.append(getvalue(mytree,mycurr))
        #myoutput += getvalue(mytree,mycurr)
    return myoutput,frame

#myoutput = driverFunc(8,100,3)
#for i in myoutput:
    #print(i)






#print("Translated File: ")
if __name__ == '__main__':
    output = driverFunc(sys.argv[2],sys.argv[1], 0)
    
print(translated)
#print("Length of translated: ", len(translated))
