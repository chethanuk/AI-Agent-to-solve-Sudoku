# Artificial Intelligence
## Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: If two boxes in same unit has exactly 2 possibilites, same unit mean that one box must be peer of other or be placed in same row or col or square unit. Finally, Two possibilites must be exactly same in both the boxes for them to be twin boxes. When, it confirmed they are twin boxes, then those two possibilites cannot be placed in anywhere else in peers of box.

No other box can have those two numbers that naked twins contain and mainly naked twin can only be filled with one of the two possiblites.

Strategy is Find the twin boxe with same two identical values in samee unit and eliminate these two in other boxes of same unit of twin boxes.

		a) Search for the posssible values [Lenth =2]
		b) Identify naked twins [Length of possibility of box == 2 and Value[box1] == Value [box2]]
		c) Using the Set Intersection [py .interstion func] to find common peers of both boxes.
		d) For each naked twin,
			Iterate through unit in unitlist with exception of naked twins.
			Remove those two in naked twins from others in unit list.
			[Remove mean Replace the digit with ''].

Search for Reduce Puzzle :

	a) If False already then return False. Check for return value if search fail then return fail.
	b) If all the boxes has len of possibilties equal to 1, it implies it solved so Return the values.
		Since, Search didn't fail return Succed / Passed.
	c) Find the box wwith least possibilties and set s equal to the box with the least number of possible values.
	d) Iterates over every possible value in the list of possible values stored in values[s].
	e) Copies the board of values. Create a new temp Values is important because if not done, all the changes will become permanent if for any  reason it fail, changes will become permanent.
	Or if any try was not correct then also those changes will become permanent. At nth attmpt if solution was not found then at n+1 th attempt board cannot be used since it was destroyed in previous attempt.
	f) Set new s and Performs a search that tries to solve the Sudoku using this current assignment.
	g) Checks for a return value.
		i) None if fails [Failed attempt should not be returned since sudoku is not solved yet].
		ii) If not failed, implies it passed.
		iii) Find a non-None value and returns if available.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
A:

	* Diagonal 1 of Sudoku is ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'].
	* Diagonal 2 of Sudoku is ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1'].

    **According to Diagonal Sudoku rule, Number 1-9 must appear exactly once in each of two diagonals, we know the Basic AI rule is apply the rules of Scenario as constraint in Constraint propgation.**

	Treat the two diagonals as extra constraints, Treating two diagonal lines as extra units and apply similar constraints of Elimination and search so it will reducee possibilites by two more level.

	diagonal_unit_hard = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'],
                      ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]
	Diagonal Elements [A1-A9] and [A9-A1]
	diagonal_units = [[s+t for s,t in zip(rows,cols)] , [s+t for s,t in zip(rows,cols[::-1])]]

    Unit List is all ROW UNITS + Col Units and Square Units

    To Solve Diagonal Sudoku set a diagonal flag with 1.
    diagonal = 1

    If diagonal flag is 1, implies it's diagonal sudoku hence Add the two diagonal lines as two extra units into unit list which already include row_units, column_units and square_units. Else If not diagonal sudoku hence, no need to treat the diagonal constraints also.

    Hence, unitlist will be just row_units, column_units and square_units.
	if diagonal == 1:
    	unitlist = row_units + column_units + square_units + diagonal_units
	else:
    	unitlist = row_units + column_units + square_units

### Input : '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

### Output Obtained :
<a href="https://ibb.co/ehC68F"><img src="https://preview.ibb.co/j6GYoF/Q.png" alt="Q" border="0"></a><br /><a target='_blank' href='http://www.pygame.org/download.shtml'>Output displayed using pygame visualization</a><br />

### Install

This project requires **Python 3**.

Install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py
