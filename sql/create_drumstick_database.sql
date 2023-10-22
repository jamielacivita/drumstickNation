CREATE DATABASE drumstickNation;
USE drumstickNation

CREATE TABLE Food (
food_index SERIAL,
food VARCHAR(25),
upc VARCHAR(10),
price DECIMAL(3,2),
serving_size_g INT(4),
servings_per_container DECIMAL(3,1),
calories INT(4),
fat_total_g INT(4),
fat_saturated_g INT(4),
fat_trans_g INT(4),
cholesterol_mg INT(4),
sodium_mg INT(4),
carbohydrates_g INT(4),
fiber_g INT(4),
sugars_total_g INT(4),
sugars_added_g INT(4),
protein_g INT(4),
food_group ENUM("vegetables","grains","fruits","protein","other"),
karma INT(3),
PRIMARY KEY(food_index)
);


