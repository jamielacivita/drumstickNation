import Food
import API

def main():

    nutritionix_request = API.Nutritionix()
    upc = "0211300507283"
    api_data = API.Nutritionix().make_request(upc)

    p = Food.Food()
    p.set_from_nutritionix_api(api_data)
    print(p)






if __name__ == "__main__":
    main()


    # "https://www.youtube.com/watch?v=j3nXYVlPrcY"

