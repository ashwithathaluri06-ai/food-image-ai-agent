from src.image_lookup import find_food_image, search_foods, get_food_details
from PIL import Image


def run_agent(food_name):
    """
    Find and display the image for a requested food item.
    """

    print("\nFood Image Agent")
    print("-" * 30)
    print(f"Searching for: {food_name}")

    # First try exact match
    image_path = find_food_image(food_name)

    if image_path:
        print("Exact food found!")
        print(f"Image: {image_path}")

        image = Image.open(image_path)
        image.show()
        return

    # If exact match is not found, try partial search
    matches = search_foods(food_name)

    if len(matches) == 0:
        print("Food not found in the dataset.")
        return

    if len(matches) == 1:
        print("One matching food found!")
        print(f"Food: {matches[0]['item_name']}")
        print(f"Image: {matches[0]['image_path']}")

        image = Image.open(matches[0]["image_path"])
        image.show()
        return

    # Multiple matches
    print("\nMultiple matching foods found:")

    for index, match in enumerate(matches, start=1):
        print(f"{index}. {match['item_name']}")

    try:
        choice = int(input("\nEnter the number of the food you want: "))

        if 1 <= choice <= len(matches):

            selected = matches[choice - 1]

            print(f"\nSelected: {selected['item_name']}")
            print(f"Image: {selected['image_path']}")

            image = Image.open(selected["image_path"])
            image.show()

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    food_name = input("Enter a food name: ")
    run_agent(food_name)