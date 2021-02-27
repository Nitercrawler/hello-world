# Read the first equation
a = int(input())
b = int(input())
c = int(input())

# Read the second equation
d = int(input())
e = int(input())
f = int(input())

solution_found = False
# apply brute force method
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x,y)

            solution_found = True
if not solution_found:
    print("No solution")
