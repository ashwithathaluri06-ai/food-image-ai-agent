import pandas as pd
import os


DATASET_FILE = "input/food_image_dataset.xlsx"


def normalize_food_name(food_name):
    """
    Normalize a food name by:
    - converting to lowercase
    - removing extra spaces
    """

    return " ".join(str(food_name).strip().lower().split())


def find_food_image(food_name):
    """
    Find the image path for a given food name.
    """

    df = pd.read_excel(DATASET_FILE)

    normalized_input = normalize_food_name(food_name)

    matches = df[
        df["item_name"]
        .astype(str)
        .apply(normalize_food_name)
        == normalized_input
    ]

    if matches.empty:
        return None

    image_path = matches.iloc[0]["image_path"]

    if os.path.exists(image_path):
        return image_path

    return None


def search_foods(search_text):
    """
    Find foods containing the search text.
    """

    if not search_text or not search_text.strip():
        return []

    df = pd.read_excel(DATASET_FILE)

    normalized_input = normalize_food_name(search_text)

    matches = df[
        df["item_name"]
        .astype(str)
        .apply(normalize_food_name)
        .str.contains(normalized_input, regex=False)
    ]

    return matches[["item_name", "image_path"]].to_dict("records")


def get_food_details(food_name):
    """
    Get complete details for a food item.
    """

    results = search_foods(food_name)

    if not results:
        return None

    return results[0]