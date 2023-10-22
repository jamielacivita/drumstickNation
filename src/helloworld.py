import  mysql.connector
import Food

def helloworld():
    return "JWTO"


def main():
    print(f"Hello JWTO.")
    database_connect()
def database_connect():
    mydb = mysql.connector.connect(host="localhost", user="jamie",password="t3g7i",database="drumstickNation")
    #print(mydb)

    bread = Food.Food()

    mycursor = mydb.cursor()
    mycursor.execute("Select calories, food_group from Food where food_index = 3")
    for x in mycursor:
        print(x)
        print(bread)

if __name__ == "__main__":
    main()
    # "https://www.youtube.com/watch?v=j3nXYVlPrcY"

