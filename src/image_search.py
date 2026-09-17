from ddgs import DDGS
import requests
import os
from src.image_quality import check_image_quality


def search_images(food_name, max_results=5, search_query=None):
    """Search the web for images of a food item."""

    if search_query is None:
        search_query = food_name + " food dish"

    with DDGS() as ddgs:
        results = list(
            ddgs.images(
                query=search_query,
                max_results=max_results
            )
        )

    return results
    with DDGS() as ddgs:
        results = list(
            ddgs.images(
                query=query,
                max_results=max_results
            )
        )

    return results


def download_image(image_url, save_path):
    """Download an image from a URL."""

    response = requests.get(
        image_url,
        timeout=15,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    with open(save_path, "wb") as file:
        file.write(response.content)

    return True


def find_best_image(food_name, output_folder="output", max_candidates=5):
    """Search multiple image candidates and retry with different queries."""

    os.makedirs(output_folder, exist_ok=True)

    search_queries = [
        food_name + " food dish",
        food_name + " authentic food",
        food_name + " restaurant dish"
    ]

    for query_number, search_query in enumerate(search_queries, start=1):

        print(f"\nSearch attempt {query_number}: {search_query}")

        results = search_images(
            food_name,
            max_results=max_candidates,
            search_query=search_query
        )

        print(f"Found {len(results)} candidates")

        for index, result in enumerate(results, start=1):

            image_url = result.get("image")

            if not image_url:
                print(f"Candidate {index}: No image URL")
                continue

            file_name = (
                food_name.lower().replace(" ", "_")
                + f"_candidate_{query_number}_{index}.jpg"
            )

            save_path = os.path.join(output_folder, file_name)

            try:
                download_image(image_url, save_path)

                print(f"Candidate {index}: Downloaded")

                is_good, message = check_image_quality(save_path)

                print(f"Candidate {index}: {message}")

                if is_good:
                    print(f"Candidate {index}: ACCEPTED")
                    return save_path

                print(f"Candidate {index}: REJECTED")

                if os.path.exists(save_path):
                    os.remove(save_path)

            except Exception as error:
                print(f"Candidate {index}: Failed - {error}")

                if os.path.exists(save_path):
                    os.remove(save_path)

        print("No good image found with this search query. Retrying...")

    print(f"\nNo suitable image found for {food_name} after all retries.")

    return None