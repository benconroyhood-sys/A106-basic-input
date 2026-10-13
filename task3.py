#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print('This python script solves for "x" with the following formula:\n\nax + b = c\n\nEnter the following variables to solve for "x"\n')
input_a = ("a: ")
a = float(input(input_a))
input_b = ("b: ")
b = float(input(input_b))
input_c = ("c: ")
c = float(input(input_c))
print()
x = (c - b) / a
print(f"x = {x}")