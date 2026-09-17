import pandas as pd
from src.image_search import find_best_image


# Excel file containing the food names
input_file = "input/food_items_clean.xlsx"


# Read the Excel file
df = pd.read_excel(input_file)

print(f"Total food items: {len(df)}")


# Process every food item
for index, row in df.iterrows():

    food_name = str(row["item_name"]).strip()

    print("\n" + "=" * 60)
    print(f"Processing {index + 1}/{len(df)}: {food_name}")
    print("=" * 60)

    try:
        result = find_best_image(food_name)

        if result:
            print(f"SUCCESS: {food_name}")
            print(f"Saved to: {result}")
        else:
            print(f"FAILED: {food_name}")

    except Exception as error:
        print(f"ERROR: {food_name}")
        print(error)


print("\n" + "=" * 60)
print("ALL FOOD ITEMS PROCESSED")
print("=" * 60)