Decision-Tree Implementation in Python using the ID3 Algorithm. ((without using any python machine learning libraries)

I have also implemented the post pruning of the tree to increase the accuracy. I have implemented two different methods of post pruning:
1.	Prune the parent node of all leaf nodes
2.	Pruning randomly selected non leaf nodes 

Here, we will randomly select n non leaf nodes to prune where n is equal to (if the no of non-leaf nodes is even) or one less than (if the no of non-leaf nodes is odd) the number of non-leaf nodes. I used python’s random class to generate node ids randomly.

You have to comment the pruning strategy in the code which you do not want to use.

Running the program:
Please follow the following steps to run the program:

1.	Download three files: DecisionTree.py, driver.py and Immunotherapy1.csv into the same folder.

2.	Install the following dependencies before running the program:
	•	pandas
	•	sklearn
	•	math
	•	random
	•	fractions

3.	You can run the files with any ide or command prompt. To run the file using command prompt, open the command prompt, navigate to the directory where the abovementioned three files are located and run the command python driver.py. The output will be displayed in command prompt.
