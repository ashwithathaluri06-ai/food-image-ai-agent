# Food Image AI Agent

A Python-based Food Image AI Agent that searches a food dataset and retrieves the corresponding food image automatically.

## Features

- Search food items by name
- Exact food-name matching
- Partial food-name search
- Multiple matching results with user selection
- Automatic food image retrieval
- Image path validation
- Handles unknown and empty inputs
- 211 food items with processed images
- Image quality and file validation
- Automatic image candidate selection and retry

## Project Structure

```text
food-image-ai-agent/
├── input/
│   └── food_image_dataset.xlsx
├── output/
│   └── processed food images
├── create_input.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── create_image_dataset.py
│   ├── food_image_agent.py
│   ├── image_lookup.py
│   ├── image_processor.py
│   ├── image_quality.py
│   ├── image_search.py
│   └── process_all_foods.py
└── tests/
    ├── test_image_search.py
    ├── test_pdf.py
    ├── test_quality.py
    ├── test_quality_check.py
    └── test_search.py
    Technologies Used
Python
Pandas
OpenPyXL
Pillow
OpenCV
DDGS / DuckDuckGo Search
Excel
Dataset

The project contains 211 unique food items with corresponding processed food images.

Validation Results
Total food items: 211
Missing image paths: 0
Images below 200x200: 0
Broken images: 0
How to Run

Activate the virtual environment and run:

python .\src\food_image_agent.py

Enter a food name when prompted.

Example:

Enter a food name: chicken tandoori

The agent finds the matching food and displays its corresponding image.

Example

For a partial search such as:

chicken

the agent displays matching food items and allows the user to select one.

Project Status

Core food search, image lookup, image processing, automatic image candidate selection and retry, validation, and user interaction features are implemented and tested.