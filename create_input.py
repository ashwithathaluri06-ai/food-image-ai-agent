from pypdf import PdfReader
import pandas as pd

PDF_PATH = "input/Ai agent - Sheet1.pdf"
OUTPUT_PATH = "input/food_items_clean.xlsx"

# Known categories
categories = [
    "Fried Rice and Noodles",
    "Rice and Biryani",
    "Soups and Salads",
    "Main Course",
    "Pizza and Pasta",
    "Starters",
    "Breads",
    "Snacks",
]

# Known subcategories
subcategories = [
    "Non Veg Starters",
    "Veg Starters",
    "Non Veg Fried Rice",
    "Veg Fried Rice",
    "Non Veg Noodles",
    "Veg Noodles",
    "Biryani",
    "Rice",
    "Breads",
    "Veg Main Course",
    "Non Veg Main Course",
    "Veg Soups",
    "Non Veg Soups",
    "Salads",
    "Snacks",
    "Veg Pasta",
    "Non Veg Pasta",
]

reader = PdfReader(PDF_PATH)

rows = []

for page in reader.pages:
    text = page.extract_text()

    if not text:
        continue

    for line in text.splitlines():
        line = line.strip()

        if not line or line.startswith("menu_category"):
            continue

        category = None
        subcategory = None
        item_name = line

        # Find category
        for cat in sorted(categories, key=len, reverse=True):
            if line.startswith(cat + " "):
                category = cat
                item_name = line[len(cat):].strip()
                break

        # Find subcategory
        if category:
            for sub in sorted(subcategories, key=len, reverse=True):
                if item_name.startswith(sub + " "):
                    subcategory = sub
                    item_name = item_name[len(sub):].strip()
                    break

        if category and subcategory and item_name:
            rows.append({
                "menu_category": category,
                "menu_sub_category": subcategory,
                "item_name": item_name
            })

# Remove duplicate food items
df = pd.DataFrame(rows)
df = df.drop_duplicates(subset=["item_name"]).reset_index(drop=True)

df.to_excel(OUTPUT_PATH, index=False)

print("Created:", OUTPUT_PATH)
print("Unique food items:", len(df))
print("\nFirst 10 items:")
print(df.head(10).to_string(index=False))