# Michael Donald # 1896510 #
# College of Technology
# The University of Houston#
# CIS 2348 - January 27, 2021   #

# # # Homework #1 #####
# Birthday Calculator #

# Current date input
print('Birthday Calculator')
print('Current Day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

# Birthday input
print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))

# How to find the age of the user
if birth_month < current_month:
    years = (current_year - birth_year)
if birth_month == current_month and birth_day > current_day:
    years = (current_year - birth_year) - 1
else:
    years = (current_year - birth_year)
if birth_month > current_month:
    years = (current_year - birth_year) - 1
if birth_month == current_month and birth_day == current_day:
    years = (current_year - birth_year)
    print('Happy Birthday')
print('You are', years, 'old.')
