import click

from .convert_aws import convert_file, convert_file_without_image

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "-O",
    "--output-file",
    default="-",
    help='Output filename (or "-" for standard output)',
    type=click.Path(dir_okay=False, writable=True, exists=False, allow_dash=True),
)
@click.argument("aws-json-file", type=click.Path(dir_okay=False, exists=True))
@click.argument("image-file", type=str)
@click.option("--image-width", type=int, help="Width of the image in pixels, if the image isn't available.")
@click.option("--image-height", type=int, help="Height of the image in pixels, if the image isn't available.")
def cli(output_file, aws_json_file, image_file, image_width, image_height):
    """Convert an AWS Textract JSON file to a PAGE XML file.

    Because of differences in the way Textract JSON and PAGE XML represent coordinates,
    either the original image file must be supplied, or the image's filename and its 
    absolute pixel dimensions must be supplied.

    The output file will reference the image file using the name you provide.
    (So you may want to use a relative path.)
    """
    if output_file == "-":
        output_file = None

    if (image_width and image_height):
        convert_file_without_image(aws_json_file, image_file, image_width, image_height, output_file)
    else:
        convert_file(aws_json_file, image_file, output_file)

if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
