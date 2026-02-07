from pathlib import Path
from joining import images_to_gif
from splitting import gif_to_images

if __name__ == "__main__":
    image_names = [
        "dog1_1920x1200.jpg",
        "dog2_1920x1200.jpg",
    ]

    image_paths = [Path("resources") / name for name in image_names]

    images_to_gif(
        image_paths=image_paths,
        output_path=Path("sample_outputs/dogs_1920x1200.gif"),
        size=(1920, 1200),
        duration=400,
    )

    gif_to_images(
        gif_path=Path("resources/michael_scott.gif"),
        output_path=Path("sample_outputs/michael_scott")
    )

    gif_to_images(
        gif_path=Path("resources/jake.gif"),
        output_path=Path("sample_outputs/jake")
    )
