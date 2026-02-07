from itertools import repeat
from PIL import Image
from multiprocessing import Pool, cpu_count
from pathlib import Path
from collections.abc import Iterable


type Size = tuple[int, int]


def _load_and_resize(path: Path, size: Size) -> Image.Image:
    with Image.open(path) as img:
        rgba_img = img.convert("RGBA")
        return rgba_img.resize(size) if rgba_img.size != size else rgba_img

def _load_and_resize_images(
    image_paths: Iterable[Path],
    size: Size,
    processes: int | None
) -> list[Image.Image]:
    with Pool(processes or cpu_count()) as pool:
        frames = pool.starmap(
            _load_and_resize,
            zip(image_paths, repeat(size))
        )

    return frames


def images_to_gif(
    image_paths: Iterable[Path],
    output_path: str | Path,
    size: Size = (256, 256),
    duration: int = 500,
    loop: int = 0,
    processes: int | None = None,
) -> None:
    """
    Convert a list of images into an animated GIF.
    Order is preserved.
    """
    if not image_paths:
        raise ValueError("No images provided.")


    frames = _load_and_resize_images(image_paths, size, processes)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
        disposal=2,
    )

    print(f"GIF saved to {output_path}")


