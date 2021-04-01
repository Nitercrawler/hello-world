# Michael Donald
# 1896510

class ItemToPurchase:

    def __init__(self, prod_item_name='none', prod_item_price=0, prod_item_quantity=0):
        self.item_price = prod_item_price
        self.item_quantity = prod_item_quantity
        self.item_name = prod_item_name

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' + str(
            self.item_price * self.item_quantity))


if __name__ == '__main__':
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print('Item 1')
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    print('Item 2')
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print('Total: $' + str(total))