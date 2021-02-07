# Michael Donald
# 1896510

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
paintColors = {'red': 35, 'blue': 25, 'green': 23}   # Paint colors red, blue, green
h = float(input('Enter wall height (feet):\n'))   # Enter number
w = float(input('Enter wall width (feet):\n'))    # Enter number

area = h * w  # area of wall

print('Wall area:', round(area), "square feet")
galls = area / 350
print('Paint needed:', round(galls, 2), "gallons")
cans = galls
print('Cans needed:', round(cans), "can(s)")
color = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing ' + color + ' paint: $' + str(cans * paintColors[color]))
