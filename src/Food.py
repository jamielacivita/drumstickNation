import get_random

class Food:
    def __init__(self):
        self.food=None
        self.upc=None
        self.price = None
        self.serving_size_g=None
        self.servings_per_container=None
        self.calories_per_serving=None
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
        print(f"Calories : {self.calories_per_serving}")
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


    def get_sql_insert(self):
        sql_str = ""
        sql_str = sql_str + "Insert into Food (\n"
        sql_str = sql_str + "food,\n"
        sql_str = sql_str + "upc,\n"
        sql_str = sql_str + "serving_size_g,\n"
        sql_str = sql_str + "servings_per_container,\n"
        #sql_str = sql_str + "calories_per_serving,\n"
        sql_str = sql_str + "calories,\n"
        sql_str = sql_str + "fat_total_g,\n"
        sql_str = sql_str + "fat_saturated_g,\n"
        sql_str = sql_str + "fat_trans_g,\n"
        sql_str = sql_str + "cholesterol_mg,\n"
        sql_str = sql_str + "sodium_mg,\n"
        sql_str = sql_str + "carbohydrates_g,\n"
        sql_str = sql_str + "fiber_g,\n"
        sql_str = sql_str + "sugars_total_g,\n"
        sql_str = sql_str + "sugars_added_g,\n"
        sql_str = sql_str + "protein_g,\n"
        sql_str = sql_str + "food_group,\n"
        sql_str = sql_str + "karma\n"
        sql_str = sql_str + ")\n"
        sql_str = sql_str + "VALUES\n"
        sql_str = sql_str + "(\n"
        sql_str = sql_str + "-- food\n"
        sql_str = sql_str + f"'{self.food}',\n"
        sql_str = sql_str + "-- UPC\n"
        sql_str = sql_str + f"'{self.upc}',\n"
        sql_str = sql_str + "-- serving size in g\n"
        sql_str = sql_str + f"'{self.serving_size_g}',\n"
        sql_str = sql_str + "-- servings per container\n"
        sql_str = sql_str + f"'{self.servings_per_container}',\n"
        sql_str = sql_str + "-- calories per serving\n"
        sql_str = sql_str + f"'{self.calories_per_serving}',\n"
        sql_str = sql_str + "-- fat_total in g\n"
        sql_str = sql_str + f"'{self.fat_total_g}',\n"
        sql_str = sql_str + "-- saturated fat in g\n"
        sql_str = sql_str + f"'{self.fat_saturated_g}',\n"
        sql_str = sql_str + "-- trans fat in g\n"
        sql_str = sql_str + f"'{self.fat_trans_g}',\n"
        sql_str = sql_str + "-- cholesterol in mg\n"
        sql_str = sql_str + f"'{self.cholesterol_mg}',\n"
        sql_str = sql_str + "-- sodium in mg\n"
        sql_str = sql_str + f"'{self.sodium_mg}',\n"
        sql_str = sql_str + "-- carbohydrates in g\n"
        sql_str = sql_str + f"'{self.carbohydrates_g}',\n"
        sql_str = sql_str + "-- fiber in g\n"
        sql_str = sql_str + f"'{self.fiber_g}',\n"
        sql_str = sql_str + "-- total sugar\n"
        sql_str = sql_str + f"'{self.sugars_total_g}',\n"
        sql_str = sql_str + "-- added sugar\n"
        sql_str = sql_str + f"'{self.sugars_added_g}',\n"
        sql_str = sql_str + "-- protein\n"
        sql_str = sql_str + f"'{self.protein_g}',\n"
        sql_str = sql_str + "-- food group\n"
        sql_str = sql_str + f"'{self.food_group}',\n"
        sql_str = sql_str + "-- karma\n"
        sql_str = sql_str + f"'{self.karma}'\n"
        sql_str = sql_str + f");\n"

        return sql_str


    def set_from_nutritionix_api(self,json_dict):
        food_dict = json_dict["foods"][0]
        self.food = food_dict["food_name"]
        self.serving_size_g = food_dict["serving_weight_grams"]
        self.servings_per_container = None
        self.calories_per_serving = food_dict["nf_calories"]
        self.fat_total_g = food_dict["nf_total_fat"]
        self.fat_saturated_g = food_dict["nf_saturated_fat"]
        self.fat_trans_g = None
        self.cholesterol_mg = food_dict["nf_cholesterol"]
        self.sodium_mg = food_dict["nf_sodium"]
        self.carbohydrates_g = food_dict["nf_total_carbohydrate"]
        self.fiber_g = food_dict["nf_dietary_fiber"]
        self.sugars_total_g = food_dict["nf_sugars"]
        self.sugars_added_g = None
        self.protein_g = food_dict["nf_protein"]
        self.food_group = None
        self.karma = "3"

        return None





