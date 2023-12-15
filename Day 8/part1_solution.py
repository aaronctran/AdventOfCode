import sys
steps, _, *rest = open(sys.argv[1]).read().splitlines()

network = {}

for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1: -1].split(", ")
    
step_count = 0
rule = "AAA"

while rule != 'ZZZ':
    step_count += 1
    rule = network[rule][0 if steps[0] == "L" else 1]
    steps = steps[1: ] + steps[0]
    
print("Steps:", step_count)