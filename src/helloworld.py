import  mysql.connector
import Food
import API
import DBconnection as database

def helloworld():
    return "JWTO"


def main():
    print(f"Hello JWTO.")
    #database_connect()
    f = Food.Food()
    f.food="McDonalds Fries"
    f.upc="None"
    f.price="3.00"
    f.serving_size_g="360"
    f.servings_per_container = "1"
    f.calories_per_serving="500"
    f.fat_total_g = "330"
    f.fat_saturated_g = "250"
    f.fat_trans_g = "50"
    f.cholesterol_mg = "30"
    f.sodium_mg = "1100"
    f.carbohydrates_g = "11"
    f.fiber_g = "99"
    f.sugars_total_g = "57"
    f.sugars_added_g = "7"
    f.protein_g = "751"
    f.food_group = "Other"
    f.karma = "0"
    #print(f)
    #mysql_string = f.get_sql_insert()

    #db = database.DBconnection()
    #db.execute_sql(mysql_string)
    nutritionix_request = API.Nutritionix("021130091317")
    broccoli_data = nutritionix_request.make_request()
    g = Food.Food()
    g.set_from_nutritionix_api(broccoli_data)
    print(g)

    nutritionix_request = API.Nutritionix("01201303")
    pepsi_data = nutritionix_request.make_request()
    p = Food.Food()
    p.set_from_nutritionix_api(pepsi_data)
    print(p)






if __name__ == "__main__":
    main()


    # "https://www.youtube.com/watch?v=j3nXYVlPrcY"

