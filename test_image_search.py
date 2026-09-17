from ddgs import DDGS

food = "Chicken Tandoori"

with DDGS() as ddgs:
    results = list(ddgs.images(
        query=food + " food",
        max_results=5
    ))

print("Images found:", len(results))

for i, result in enumerate(results, start=1):
    print(f"\n{i}.")
    print("Title:", result.get("title"))
    print("Image URL:", result.get("image"))