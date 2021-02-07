# Michael Donald
# 1896510

print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')
shop_service1 = input('Select first service:\n')  # asking user to enter service 1
shop_service2 = input('Select second service:\n')  # asking user to enter service 2
total_service_amount=0  # variable to store service total amount
print('\nDavy\'s auto shop invoice\n')  # print invoice

if shop_service1.lower() == "oil change":  # oil change service
    print('Service 1: Oil change, $35')  # print oil change details
    total_service_amount = total_service_amount + 35  # add oil change $35 to total
elif shop_service1.lower() == "tire rotation":  # tire rotation service
    print('Service 1: Tire rotation, $19')  # print Tire rotation, $19
    total_service_amount = total_service_amount + 19  # add tire rotation $19 to total
elif shop_service1.lower() == "car wash":  # car wash
    print('Service 1: Car Wash, $7')  # print car wash $7
    total_service_amount = total_service_amount + 7  # add car wash $7 to total
elif shop_service1.lower() == "car wax":  # car wax Service
    print('Service 1: Car Wax, $12\n')  # print car wax $12
    total_service_amount = total_service_amount + 12  # add car wax $12 to total
elif shop_service1 == "-":  # when no service
    print('Service 1: No service')
if shop_service2.lower() == "oil change":  # when oil change service
    print('Service 2 Oil change, $35')  # print oil change $35
    totalServiceAmount = total_service_amount + 35  # add oil change cost $35 to total
elif shop_service2.upper() == "tire rotation":  # tire rotation service
    print('Service 2: Tire rotation, $19')  # print Tire rotation, $19
    total_service_amount = total_service_amount + 19  # add tire rotation $19 to total
elif shop_service2.lower() == "car wash":  # car wash
    print('Service 2: Car wash, $7\n')  # print car wash $7
    total_service_amount = total_service_amount + 7  # add car wash $7 to total
elif shop_service2.lower() == "car wax":  # car wax Service
    print('Service 2: Car wax, $12\n')  # print car wax $12
    total_service_amount = total_service_amount + 12  # add car wax $12 to total
elif shop_service2 == "-":  # no service
    print('Service 2: No service\n')

print('Total: $',total_service_amount)

