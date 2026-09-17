from src.image_processor import process_image
import os

input_path = "output/chicken_tandoori_test.jpg"
output_path = "output/Chicken Tandoori.jpg"

os.makedirs("output", exist_ok=True)

result = process_image(input_path, output_path)

print("Image processed successfully!")
print("Width:", result["width"])
print("Height:", result["height"])
print("File size:", result["file_size_mb"], "MB")
print("JPEG quality:", result["quality"])
print("Saved to:", output_path)