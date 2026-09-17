from PIL import Image, ImageOps
import os


TARGET_WIDTH = 1800
TARGET_HEIGHT = 1200
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def process_image(input_path, output_path):
    """
    Resize and compress an image to 1800x1200 JPG.
    """

    image = Image.open(input_path).convert("RGB")

    # Resize while keeping the image proportional
    image.thumbnail((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)

    # Create 1800x1200 canvas
    canvas = Image.new(
        "RGB",
        (TARGET_WIDTH, TARGET_HEIGHT),
        "white"
    )

    # Center the image without unnecessary cropping
    x = (TARGET_WIDTH - image.width) // 2
    y = (TARGET_HEIGHT - image.height) // 2

    canvas.paste(image, (x, y))

    quality = 90

    # Save as JPG
    canvas.save(
        output_path,
        "JPEG",
        quality=quality,
        optimize=True
    )

    # Reduce quality if file is above 10 MB
    while os.path.getsize(output_path) > MAX_FILE_SIZE and quality > 30:

        quality -= 5

        canvas.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True
        )

    return {
        "width": canvas.width,
        "height": canvas.height,
        "file_size_mb": round(
            os.path.getsize(output_path) / (1024 * 1024),
            2
        ),
        "quality": quality
    }