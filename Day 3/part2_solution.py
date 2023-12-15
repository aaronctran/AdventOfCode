import sys

# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.
# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.
# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:
    # 467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598..
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

grid = open(sys.argv[1]).read().split()
total = 0

for r, row in enumerate(grid):                  # Gets the row index and the actual row
    for c, ch in enumerate(row):                # c is for the coordinates and ch is the actual character
        if ch != "*":           # Skips if the char is either a digit or a period 
            continue
        
        cs = set()
        # Scan a 3x3 region around the special character
        for cr in [r -1, r, r + 1]:         
            for cc in [c - 1, c, c + 1]:
                # This if statement checks for out of bounds
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc - 1].isdigit():    # Loops to find a digit 
                    cc -= 1
                cs.add((cr, cc))                                # Adds the coordinates (Row Index, Char Index)of the first digit of the actual digit to the set
        
        if len(cs) != 2:
            continue
        
        nums = []

        for cr, cc in cs:
            num = ""
            while c < len(grid[cr]) and grid[cr][cc].isdigit():            # Loops thru to grab the entire digit 
                num += grid[cr][cc]
                cc += 1
            nums.append(int(num))
        
        total += nums[0] * nums[1]
print(total)