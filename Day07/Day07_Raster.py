from PIL import Image

# Data source: https://visibleearth.nasa.gov/images/73909/december-blue-marble-next-generation-w-topography-and-bathymetry/73911l
world_topography = Image.open("Day07/data/NASA_blue_marble.jpg")
output_path = "Day07/NASA_blue_marble_resampled.jpg"

def sampling(input, output, factor, resampling_type=4) -> None:
    """Resampling image based on an input file, a resampling factor
    which floor-divides the image using the factor as divisor. The resampling
    type corresponds to the filters from the pillow library (0=nearest, 1=lanczos,
    ... 4=box)

    Args:
        input (image): Input path of image.
        output (image): Output path of image.
        factor (int): Divisor that width and height of the image is floor-divded by.
        resampling_type (int, optional): Resampling type, box (4) is default to create a coarse raster representation.
    """

    downsampling = input.resize((input.width//factor, input.height//factor), resample=resampling_type)
    upsampling = downsampling.resize(input.size, resample=resampling_type)
    upsampling.save(output)

sampling(world_topography, output_path, 100)