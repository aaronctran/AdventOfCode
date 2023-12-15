import sys
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving. "Aaah!"
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:
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
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

grid = open(sys.argv[1]).read().split()         
cs = set()                                      # Coordinate set

for r, row in enumerate(grid):                  # Gets the row index and the actual row
    for c, ch in enumerate(row):                # c is for the coordinates and ch is the actual character
        if ch.isdigit() or ch == ".":           # Skips if the char is either a digit or a period 
            continue
        # Scan a 3x3 region around the special character
        for cr in [r -1, r, r + 1]:         
            for cc in [c - 1, c, c + 1]:
                # This if statement checks for out of bounds
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc - 1].isdigit():    # Loops to find a digit 
                    cc -= 1
                cs.add((cr, cc))                                # Adds the coordinates (Row Index, Char Index)of the first digit of the actual digit to the set
nums = []

for r, c in cs:
    num = ""
    while c < len(grid[r]) and grid[r][c].isdigit():            # Loops thru to grab the entire digit 
        num += grid[r][c]
        c += 1
    nums.append(int(num))
print(sum(nums))