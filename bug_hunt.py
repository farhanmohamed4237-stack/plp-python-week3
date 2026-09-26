# Week 3 Assignment - Part B: Bug Hunt

count = 1
total = 0

# BUG 1: The while statement was missing a colon.
# BUG 2: count < 5 excluded the number 5. Changed it to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG 3: The original code tried to combine text with an integer.
# Converted total to a string using str().
print("Sum of 1 to 5 is: " + str(total))
