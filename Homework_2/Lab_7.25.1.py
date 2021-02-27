def exact_change(input_value):
    # input_val = int(input())

    if input_value <= 0:
        print('no change')
        return 0,0,0,0,0
    else:
        num_dollars = input_value // 100
        input_value %= 100
        num_quarters = input_value // 25
        input_value %= 25
        num_dimes = input_value // 10
        input_value %= 10
        num_nickels = input_value // 5
        input_value %= 5
        num_pennies = input_value
        return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_value = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_value)

    if num_dollars > 1:
        print('%d dollars' % num_dollars)
    elif num_dollars == 1:
        print('%d dollar' % num_dollars)
    if num_quarters > 1:
        print('%d quarters' % num_quarters)
    elif num_quarters == 1:
        print('%d quarter' % num_quarters)
    if num_dimes > 1:
        print('%d dimes' % num_dimes)
    elif num_dimes == 1:
        print('%d dime' % num_dimes)
    if num_nickels > 1:
        print('%d nickels' % num_nickels)
    elif num_nickels == 1:
        print('%d nickel' % num_nickels)
    if num_pennies > 1:
        print('%d pennies' % num_pennies)
    elif num_pennies == 1:
        print('%d penny' % num_pennies)
