import get_random as gr

def test_helloworld():
    with open(r"/home/jamie/PycharmProjects/drumstickNation/data/food_names_random") as f:
        data = f.readlines()
    f.close()

    assert gr.get_random_food_name() in data