from config import APP_NAME, SLIDESHOW_INTERVAL
from mock_data import PHOTOS

def get_next_index(current_index):
    return current_index + 1

def main():
    current_index = 0
    current_photo = PHOTOS[current_index]

    print(f"{APP_NAME} starting...")
    print(f"Slideshow interval: {SLIDESHOW_INTERVAL}s")
    print(f"Loaded {len(PHOTOS)} photos")
    print(f"Current photo ID: {current_photo['id']}")
    print(f"Current photo filename: {current_photo['filename']}")

    current_index = get_next_index(current_index)
    current_photo = PHOTOS[current_index]

    print("Moved to next photo")
    print(f"Current photo ID: {current_photo['id']}")
    print(f"Current photo filename: {current_photo['filename']}")


if __name__ == "__main__":
    main()

