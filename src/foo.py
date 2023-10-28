class FoodList():
    def __init__(self):
        self.total_list = []
        self.selection_list = []
        self.master_list = []

        self.input_food_names_eaten()
        #self.total_list.append("Apple")
        #self.total_list.append("Approcts")

        #self.total_list.append("Bannana")
        #self.total_list.append("Carrots")
        #self.total_list.append("Dog Treates")


        for item in self.total_list:
            self.selection_list.append(item.strip())

    def input_food_names_eaten(self):
        with open("/home/jamie/PycharmProjects/drumstickNation/data/food_names_eaten.txt") as f:
            data = f.readlines()
        for d in data:
            self.total_list.append(d)
        f.close()

    def print_selection_list(self):
        index = 0
        for item in self.selection_list:
            index = index + 1
            print(f"{index}.) {item}")
        return None


    def get_user_input(self):
        user_selection = input("Select letter / number : ")
        return user_selection


    def update_selection_list(self, user_selection):
        new_list = []

        for item in self.selection_list:
            if user_selection in item:
                new_list.append(item)
                print(f"{item}")
            else:
                #print(f"discard {item}.")
                pass

        self.selection_list = []
        print(f"Length of selection list after clearing : {len(self.selection_list)}")
        for item in new_list:
            self.selection_list.append(item)
        print(f"Length of selection list after update : {len(self.selection_list)}")

    def main_loop(self):
        while len(self.selection_list) > 1:
            self.print_selection_list()
            user_selection = self.get_user_input()
            self.update_selection_list(user_selection=user_selection)
        else:
            print("\n\n")
            print(f"Selection : {self.selection_list[0]}")
            self.master_list.append(self.selection_list[0])
            for item in self.total_list:
                self.selection_list.append(item.strip())
            for item in self.master_list:
                print(f"{item}")
            print(f"----------")
            self.main_loop()

def main():
    my_list = FoodList()
    my_list.main_loop()




if __name__ == "__main__":
    main()

