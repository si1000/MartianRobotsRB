# MartianRobotsRB
 
Summary:

The script will convert the file to a dictionary for each of the robot start positions and instructions respectively. It will also get the max coordinates of the rectangle so that a perimeter can be outlined. 

It will then loop through the dictionary in order to apply each instruction one by one, so that the appropriate action can be taken if the robot is to be lost in a certain position and we can store where this was, so that the next robot will pass on the same instruction.

Each robot has its own dictionary and that is updated accordingly when an instruction is applied. Until we have gone through all the robots and their respective instructions in order to produce the desired output which is then written to a file.

Notable points (things I would do if I had more time):
•	There has not been a massive amount of error handling, so please ensure data follows same format as input data samples

•	I have avoided repeated/too much commentary

•	Given a bigger timeframe there can be more refactoring done and there could be much more efficient ways of achieving the same result using other modules. 

•	input & output file names have been hardcoded they would normally be put in a config file or specified at runtime


Runtime instructions 

1.	Create/Edit input file:
-	This is a flat text file; you can edit the existing one in the project directory.
-	If you do choose to create 
-	In the project root directory “files/input_robots.txt”
-	You may enter the rectangle coordinate size and each robot initial position and its respective instructions.
-	Please ensure that the format is correct and only correct/acceptable values are entered. Main rectangle coordinates must not exceed 50, 50
-	E.g. 

5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
	
(Exact format as the sample data provided)


2.	Execute the program from your command-line
-	Run the following: “python3 martain_robots.py”
Note: please ensure you have python3 installed and running https://www.python.org/downloads/

3.	Locate the output file:
-	The output of the program will be a file (“files/output_robots.txt”) located in the project root directory which will be in the same directory as the input file. The console will also show the input information of the robot and the output location of the robot.
