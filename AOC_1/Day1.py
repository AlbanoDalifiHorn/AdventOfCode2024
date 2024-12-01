file = open("AOC_1.txt", "r")

result = 0
counter = 0

# split my file list into two different lists
left_values = [line.split()[0] for line in file]
left_values.sort()
print(left_values)

file.seek(0)

right_values = [line.split()[1] for line in file]
right_values.sort()
print(right_values)

left_values = [int(value) for value in left_values]
right_values = [int(value) for value in right_values]

"""
Solution for Part 1
for i in range(len(left_values)):
    result += abs(left_values[i] - right_values[i])
"""

"""
Solution for Part 2
for value in left_values:
    if right_values.__contains__(value):
        for i in range(right_values.__len__()):
            if right_values[i] == value:
                counter += 1
        result += value * counter
        counter = 0
"""
print(result)
