from DecisionTree import *
import pandas as pd
from sklearn import model_selection

df= pd.read_csv('Immunotherapy1.csv')

lst = df.values.tolist()

# Genearating a decision tree for entire dataset
t = build_tree(lst, header,0,0)
print("the decision tree for entire dataset is ")
print_tree(t)

print("********** Leaf nodes ****************")
leaves = getLeafNodes(t)

for leaf in leaves:
    print("id = " + str(leaf.id) + " depth =" + str(leaf.depth))
print("********** Non-leaf nodes ****************")
innerNodes = getInnerNodes(t)

for inner in innerNodes:
    print("id = " + str(inner.id) + " depth =" + str(inner.depth))

# Spliting the dataset into training and test dataset
trainDF, testDF = model_selection.train_test_split(df, test_size=0.2)
train = trainDF.values.tolist()
test = testDF.values.tolist()
# Building decision tree for training dataset
t = build_tree(train, header,0,0)
print("the decision tree for training dataset is ")
print("*************Tree before pruning*******")
print_tree(t)
# calculate the accuracy of built tree
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))

 You have to decide on a pruning strategy
print(" ")

nodesRange=[]
print("********** Leaf nodes ****************")
leaves = getLeafNodes(t)



innerNodes = getInnerNodes(t)

for inner in innerNodes:
    nodesRange.append(inner.id)
import random
import math
nodePruned=[]
# Random Pruning 
for i in range(math.floor(len(nodesRange)/2)):
    nodePruned.append(random.choice(nodesRange))   


# Pruning parent node of all leaf nodes
#for leaf in leaves:
#    if (leaf.id)%2==0:
#        nodePruned.append(int((leaf.id)/2)-1)
#    else:
#        nodePruned.append(math.floor((leaf.id)/2))
    
    
#    nodePruned = [int(n) for n in input('Enter the ID of nodes to be pruned ').split()]
print("NodePrunedList  ",nodePruned)
t_pruned = prune_tree(t,nodePruned)
    
print("*************Tree after pruning*******")
print_tree(t_pruned)
leaves=getLeafNodes(t_pruned)
acc = computeAccuracy(test, t_pruned)
print("Accuracy on test = " + str(acc))
