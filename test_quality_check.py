from src.image_quality import check_image_quality

image_path = "output/Chicken Tandoori.jpg"

is_good, message = check_image_quality(image_path)

print("Quality check passed:", is_good)
print("Message:", message)