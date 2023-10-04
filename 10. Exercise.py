from simpleai.search import CspProblem, backtrack

# variables
input = input("Input: ")
originalList = []
uniqueList = []
beforePlus = []
beforeEquals = [] 
afterEquals = []
domains = {}

# put the input in a list using recursion
def inputToList(input):
    if (len(input)==0):
        return list
    else:
        if input[0] != ' ':
            originalList.append(input[0])
        return inputToList(input[1:])

# run the function
inputToList(input)

# put all the characters before the "+" in a seperate list
for char in originalList:
    if char != '+':
        beforePlus.append(char)
    else:
        break

# put all the characters after the "+" but before the "=" in a seperate list
for char in originalList[len(beforePlus)+1:]:
    if char != '=':
        beforeEquals.append(char)
    else:
        break

# put all the characters after the "=" in a seperate list
afterEquals = originalList[len(beforePlus) + 1 + len(beforeEquals) + 1:]

# put all the unique characters in a seperate list
for char in originalList:
    if char not in uniqueList and char != '+' and char != '=':
        uniqueList.append(char)

# set the unique list in the dictionary
def UniqueListToDictionary(uniqueList):
    if (len(uniqueList)==0):
        return domains
    else:
        # if the letter in the unique list matches the first letter of the word before "+",
        # before "=" and after "=" then range it from 1 to 10
        if uniqueList[0] == beforePlus[0] or uniqueList[0] == beforeEquals[0] or uniqueList[0] == afterEquals[0]:
            domains[uniqueList[0]] = list(range(1, 10))
        else:
            # otherwise range it from 0 to 10
            domains[uniqueList[0]] = list(range(0, 10))
        return UniqueListToDictionary(uniqueList[1:])

# run the function
UniqueListToDictionary(uniqueList)

# convert the uniqueList to a tupple called variables
variables = tuple(uniqueList)

def constraint_unique(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

def constraint_add(variables, values):
    # Ensure that each variable corresponds to a unique digit
    if len(set(values)) != len(values):
        return False

    # Convert the variables values into ints
    var_values = {variables[i]: values[i] for i in range(len(variables))}

    # Extract the left and right operands as strings
    left_operand = ''.join([str(var_values[char]) for char in beforePlus])
    right_operand = ''.join([str(var_values[char]) for char in beforeEquals])
    result = ''.join([str(var_values[char]) for char in afterEquals])

    # Check if the equation is valid (left_operand + right_operand == result)
    return int(left_operand) + int(right_operand) == int(result)

constraints = [
    (variables, constraint_unique),
    (variables, constraint_add),
]

problem = CspProblem(variables, domains, constraints)

output = backtrack(problem)
print('\nSolutions:', output)