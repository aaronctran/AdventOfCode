import sys

# Part 1
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
f = open(str(sys.argv[1]), "r")
lines = f.readlines()
symbols = "! @ # $ % ^ & * ( ) - + ? _ = , < > /".split()

# Method to get indices of each special character 
def getCharIndices(text, specialChars):
    indices = {}
    for char in specialChars:
        pattern = re.escape(char)
        matches = [match.start() for match in re.finditer(pattern, text) if match.start() == match.end() - 1]
        if matches:
            indices[char] = matches
    return indices

for i in range(1, len(lines)):
    numIndices = {}
    nums = set(lines[i - 1].strip().split("."))
    nums.remove('')
    

    charIndices = getCharIndices(lines[i - 1], symbols)
    if len(charIndices) == 0:
        charIndices = getCharIndices(lines[i], symbols)
    
    for n in nums:
        if lines[i - 1].index(n) > -1:
            # for char in charIndices:
            #     if charIndices[char] >= lines[i - 1].index(n) or charIndices[char]  len(n)
            numIndices[n] = lines[i - 1].index(n)
    print(numIndices)
    

