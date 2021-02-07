# Michael Donald
# 1896510

# FIXME (1): Finish reading other items into variables, then output the three ingrdients

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons

num_lemon_cups = float(input('Enter amount of lemon juice (in cups):\n'))  # Cups of lemon juice
num_water_cups = float(input('Enter amount of water (in cups):\n'))  # Cups of water
num_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))   # Amount of agave nectar
num_servings_cups = float(input('How many servings does this make?\n'))  # This makes six servings 

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_cups))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups))
print('{:.2f} cup(s) water'.format(num_water_cups))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups))

num_servings_required = float(input('\nHow many servings would you like to make?\n')) # How many serving

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups))
print('{:.2f} cup(s) water'.format(num_water_cups * num_servings_required / num_servings_cups))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} gallon(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups / 16))
print('{:.2f} gallon(s) water'.format(num_water_cups * num_servings_required / num_servings_cups / 16))
print('{:.2f} gallon(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups / 16))
