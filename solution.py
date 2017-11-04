assignments = []
 # defining the ROWS of SUDOKU : 
 #       rows will be labelled by the letters A, B, C, D, E, F, G, H, I.
rows = 'ABCDEFGHI'
# defining the COLUMNS of SUDOKU
#        columns will be labelled by the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9.
cols = '123456789'
all_digits = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    # cross functions take argument a and b, return the list formed after all 
    # possible concatenations of a letter s in string a with a letter t in string b.
    return [s+t for s in A for t in B]

boxes = cross(rows, cols) # creating label of boxes 
row_units = [cross(r, cols) for r in rows] # defining rows of Sudoku
column_units = [cross(rows, c) for c in cols] # defining rows of Sudoku
# Defining Square Unit (3 * 3 Boxes)
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# hardcoded
# diagonal_unit_hard = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'],
#              ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]
 # Diagonal Elements [A1-A9] and [A9-A1]
diagonal_units = [[s+t for s,t in zip(rows,cols)] , [s+t for s,t in zip(rows,cols[::-1])]]

# Unit List is all ROW UNITS + Col Units and Square Units
diagonal = 1

if diagonal == 1:
    unitlist = row_units + column_units + square_units + diagonal_units
else:
    unitlist = row_units + column_units + square_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find the posssible values in the box must be exactly two
    possible_twins = [box for box in values.keys() if len(values[box]) == 2]
    # Find Naked twins
    # naked twins is unordered collection of two unique elements 
    # for all possible_twins,[ for peers of box1] compare set of values in box1 with set of values in peer box2 and check if they are equal
    naked_twins = [[box1,box2] for box1 in possible_twins for box2 in peers[box1] \
                   if set(values[box1])==set(values[box2])]

    # Eliminate the naked twins as possibilities for their peers
    
    #Iterate from 1 to len of naked_twins
    #Find comman peers [Perform Intersection &]
    #Now, delete the two digits of naked_twins from all common peers.               
    for i in range(len(naked_twins)):
        # Assign 0th index of ith naked_twins to box1
        box1 = naked_twins[i][0]
        # Assigns 1h index of ith naked_twins to box2
        box2 = naked_twins[i][1]
        
        # Find peers of box 1 and box 2
        peers1 = set(peers[box1])
        peers2 = set(peers[box2])

        # Find common peers use & or .intersection
        # NOT WORKING common_peers = peers1 & peers2
        peers_intersect = peers1.intersection(peers2)

        # delete the 2 digits from all common_peers
        for peer_value in peers_intersect:
            #for any boxes in the peer sets that are not defined as naked twins yet have a matching value as naked twins
            if len(values[peer_value]) > 2:
                for remaining_value in values[box1]:
                    #eliminate the naked twin values from all peers
                    values = assign_value(values, peer_value, values[peer_value].replace(remaining_value, ''))
    return values

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers


def naked_twinas(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    """
    Finding all naked twins involves two conditions to satisfy
        a) Number of posssible values in the box must be exactly two
        b) Values in both box must be same and both boxes be in Same Unit [One is Peer of other]
    """
    # Find the posssible values in the box must be exactly two
    possibilities = [box for box in values.keys() if len(values[box]) == 2]
    # Find Naked twins
    naked_twins = [[box1,box2] for box1 in possibilities \
                               for box2 in peers[box1] \
                               if set(values[box1]) == set(values[box1])]
    # Eliminate the naked twins as possibilities for their peers
    
    #Iterate from 1 to len of naked_twins
    #Find comman peers [Perform Intersection &]
    #Now, delete the two digits of naked_twins from all common peers.
    
    for i in range(len(naked_twins)):
        # Assign 0th index of ith naked_twins to box1
        box1 = naked_twins[i][0]
        # Assigns 1h index of ith naked_twins to box2
        box2 = naked_twins[i][1]
        # Find peers of box 1 and box 2
        peers1 = set(peers[box1])
        peers2 = set(peers[box1])
        # Find common peers use & or .intersection
        # NOT WORKING common_peers = peers1 & peers2
        common_peers = peers1.intersection(peers2)

        # delete the 2 digits from all common_peers
        for peer in common_peers:
            if len(values[peer])>2:
                for val in values[box1]:
                    values = assign_value(values, peer, values[peer].replace(val,''))
    # reutrn the values
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    # For each i in the frid, Check if its empty if so Assign all_digits other wise just append i
    
    all_digits = '123456789'
    values = []
    for i in grid:
        # Check if ith grid is empty
        if i == '.':
            # Assign all_digits to ith place of grid
            values.append(all_digits)
        # else if Ith place has some digit just append i
        elif i in all_digits:
            values.append(i)
    # Assert condition : Since 9 * 9 sudoku it must be 81        
    assert len(values) == 81
    # return the dictionary formed after passing boxed and input grid through zip func.
    return dict(zip(boxes, values))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
             values = assign_value(values, peer, values[peer].replace(digit,''))
    return values

    solved_values = [box for box in values.keys() if len(values[box]) == 1]

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                # values[dplaces[0]] = digit
                values = assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values) 
        # Use naked twins
        values = naked_twins(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with  zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
             return False
    return values


def search(values):
    
    # First reduce the puzzle
    values = reduce_puzzle(values)
    # Failed omplies error
    if values is False:
        return False
    
    # Solved : If all the values are single digit    
    if all(len(values[s]) == 1 for s in boxes):
        return values
    
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku = assign_value(new_sudoku, s, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    # return search(grid_values(grid))

    values = grid_values(grid)
    values = search(values)

    return values

if __name__ == '__main__':
    #puzzleString =  '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    diag_sudoku_easy = '4.26.9.155...1..2..81..5.7.....6..98.........39..5.....4.1..95..5..4...226.5.83.1'
    diag_sudoku_hard = '1..4......4386....2.69...4.......52..37.....85..56.......8...57.4...1986......8..1'
    display(solve(diag_sudoku_grid))
    
    #display(solve(diag_sudoku_grid))
    
    # Test 1 
    #values = grid_values(diag_sudoku_grid)
    #display(values)
    #display(solve(diag_sudoku_grid))

    # Test 2
    #grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    #print("Values of Grid 2: ")
    #values = grid_values(grid2)

    #display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
