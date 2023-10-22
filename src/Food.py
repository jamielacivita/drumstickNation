import get_random

class Food:
    def __init__(self):
        self.food=None
        self.upc=None
        self.price = None
        self.serving_size_g=None
        self.servings_per_container=None
        self.calories=None
        self.fat_total_g=None
        self.fat_saturated_g=None
        self.fat_trans_g=None
        self.cholesterol_mg=None
        self.sodium_mg=None
        self.carbohydrates_g=None
        self.fiber_g=None
        self.sugars_total_g=None
        self.sugars_added_g=None
        self.protein_g=None
        self.food_group=None
        self.karma=None

    def set_from_tuple(self, tuple):
        self.key = tuple[0]
        self.food = tuple[1]
        self.upc=tuple[2]
        self.price=tuple[3]
        self.serving_size_g=tuple[4]
        self.servings_per_container=tuple[5]
        self.calories=tuple[6]
        self.fat_total_g=tuple[7]
        self.fat_saturated_g=tuple[8]
        self.fat_trans_g=tuple[9]
        self.cholesterol_mg=tuple[10]
        self.sodium_mg=tuple[11]
        self.carbohydrates_g=tuple[12]
        self.fiber_g=tuple[13]
        self.sugars_total_g=tuple[14]
        self.sugars_added_g=tuple[15]
        self.protein_g=tuple[16]
        self.food_group=tuple[17]
        self.karma=tuple[18]

    def __str__(self):
        print(f"Food : {self.food}".strip())
        print(f"UPC : {self.upc}")
        print(f"Price : ${self.price}")
        print(f"Servings per container : {self.servings_per_container}")
        print(f"Calories : {self.calories}")
        print(f"Total fat : {self.fat_total_g}")
        print(f"Saturated fat : {self.fat_saturated_g}")
        print(f"Trans fat : {self.fat_trans_g}")
        print(f"Cholestrol : {self.cholesterol_mg}")
        print(f"Sodium : {self.sodium_mg}")
        print(f"Total Carbohydrates : {self.carbohydrates_g}")
        print(f"Fiber : {self.fiber_g}")
        print(f"Total Sugards : {self.sugars_total_g}")
        print(f"Added Sugars : {self.sugars_added_g}")
        print(f"Protein : {self.protein_g}")
        return ""

    def make_random(self):
        self.food = get_random.get_random_food_name()
        self.upc = get_random.get_random_upc()
        self.price = None
        self.serving_size_g=None
        self.servings_per_container=None
        self.calories=None
        self.fat_total_g=None
        self.fat_saturated_g=None
        self.fat_trans_g=None
        self.cholesterol_mg=None
        self.sodium_mg=None
        self.carbohydrates_g=None
        self.fiber_g=None
        self.sugars_total_g=None
        self.sugars_added_g=None
        self.protein_g=None
        self.food_group=None
        self.karma=None

