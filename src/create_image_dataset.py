import pandas as pd
import os


# Input Excel file
input_file = "input/food_items_clean.xlsx"

# Output folder containing images
output_folder = "output"

# New Excel file
output_file = "input/food_image_dataset.xlsx"


# Read food items
df = pd.read_excel(input_file)


# Create image filename mapping
image_files = os.listdir(output_folder)

image_mapping = {}

for file in image_files:

    if not file.lower().endswith(".jpg"):
        continue

    image_name = file.replace("_candidate_1_1.jpg", "")
    image_name = image_name.replace("_candidate_1_2.jpg", "")
    image_name = image_name.replace("_candidate_1_3.jpg", "")
    image_name = image_name.replace("_candidate_1_4.jpg", "")
    image_name = image_name.replace("_candidate_1_5.jpg", "")
    image_name = image_name.replace("_candidate_2_1.jpg", "")
    image_name = image_name.replace("_candidate_2_2.jpg", "")
    image_name = image_name.replace("_candidate_2_3.jpg", "")
    image_name = image_name.replace("_candidate_2_4.jpg", "")
    image_name = image_name.replace("_candidate_2_5.jpg", "")

    image_mapping[image_name] = file


# Add image filename column
df["image_file"] = df["item_name"].apply(
    lambda x: image_mapping.get(
        str(x).strip().lower().replace(" ", "_"),
        ""
    )
)


# Add image path column
df["image_path"] = df["image_file"].apply(
    lambda x: os.path.join(output_folder, x) if x else ""
)


# Save dataset
df.to_excel(output_file, index=False)


print("Dataset created successfully!")
print(f"Total food items: {len(df)}")
print(f"Images mapped: {df['image_file'].ne('').sum()}")
print(f"Missing images: {df['image_file'].eq('').sum()}")
print(f"Saved to: {output_file}")