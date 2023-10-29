import Food
import API

def main():

    nutritionix_request = API.Nutritionix()
    #upc = "0211300507283"
    upc = "011110970305"

    api_data = API.Nutritionix().make_request(upc)

    p = Food.Food()
    p.set_from_nutritionix_api(api_data)
    print(p)
    p.scale_to_serving_size(45)
    print(p)







if __name__ == "__main__":
    main()


    # "https://www.youtube.com/watch?v=j3nXYVlPrcY"

