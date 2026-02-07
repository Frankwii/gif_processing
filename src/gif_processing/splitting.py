import math
from multiprocessing import Pool, cpu_count
from pathlib import Path

from PIL import Image, ImageSequence


def split_gif(path: Path) -> list[Image.Image]:
    with Image.open(path) as im:
        frames = [frame.copy().convert("RGBA") for frame in ImageSequence.Iterator(im)]

    return frames

def _save_image(img: Image.Image, path: Path) -> None:
    img.save(path)

def gif_to_images(
    gif_path: Path,
    output_path: Path | None = None,
    processes: int | None = None
) -> None:
    print(gif_path)
    output_path = output_path or Path(gif_path.stem)

    if not gif_path.suffix == ".gif":
        raise ValueError("File provided for GIF splitting hasn't a '.gif' extension.")

    images = split_gif(gif_path)

    n_images = len(images)
    max_digits = math.floor(math.log10(n_images)) + 1

    # This arcane math and f-string syntax is for padding with zeros to the left
    output_paths = [
        output_path.parent / f"{i:0{max_digits}}_{output_path.stem}.png"
        for i in range(len(images))
    ]

    with Pool(processes or cpu_count()) as pool:
        pool.starmap(
            _save_image,
            zip(images, output_paths)
        )
