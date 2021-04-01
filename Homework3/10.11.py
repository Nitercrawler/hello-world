# Michael Donald
# 1896510

class FoodItem:
    # TODO: Define constructor with parameters to initialize instance
    #       attributes (name, fat, carbs, protein)

    def __init__(self, product_name='None', fat_amount=0.0, carbs_amount=0.0, protein_amount=0.0):
        self.protein = protein_amount
        self.fat = fat_amount
        self.carbs = carbs_amount
        self.name = product_name

    def get_calories(self, number_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * number_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food_item1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())

    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item1.get_calories(num_servings)))

    print()

    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item2.get_calories(num_servings)))
