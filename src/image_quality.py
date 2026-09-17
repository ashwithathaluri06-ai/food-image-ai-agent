from PIL import Image
import cv2
import numpy as np


def check_image_quality(image_path):
    """
    Check whether an image is suitable for processing.
    """

    try:
        image = Image.open(image_path)

        width, height = image.size

        # Minimum resolution
        if width < 800 or height < 600:
            return False, f"Too small: {width}x{height}"

        # Convert to grayscale for blur detection
        img = cv2.imread(image_path)

        if img is None:
            return False, "Could not read image"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Variance of Laplacian measures sharpness
        blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

        if blur_score < 50:
            return False, f"Too blurry: {blur_score:.2f}"

        return True, f"Good quality: {width}x{height}, sharpness={blur_score:.2f}"

    except Exception as e:
        return False, f"Error: {e}"