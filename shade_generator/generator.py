import click

# Representation of an RGBA color.
Color = tuple[int, int, int, int]


@click.command()
@click.option('--start-color', required=True, type=(int, int, int, int), help='First color.')
@click.option('--end-color', required=True, type=(int, int, int, int), help='Last color.')
@click.option('--amount', required=True, type=int, help='Number of shades to generate.')
def generate(start_color: Color, end_color: Color, amount: int):
    shades = portion_colors(start_color, end_color, amount)

    print_color(start_color, 1)

    acc = 2
    for shade in shades:
        print_color(shade, acc)
        acc += 1

    print_color(end_color, acc)


def print_color(color: Color, num: int):
    click.echo(f"Color #{num} -> ", nl=False)
    click.secho(f"r: {color[0]} ", fg="red", nl=False)
    click.secho(f"g: {color[1]} ", fg="green", nl=False)
    click.secho(f"b: {color[2]} ", fg="blue", nl=False)
    click.secho(f"a: {color[3]}")


def portion_colors(begin_color: Color, end_color: Color, amount: int) -> list[Color]:
    reds = portion(begin_color[0], end_color[0], amount)
    greens = portion(begin_color[1], end_color[1], amount)
    blues = portion(begin_color[2], end_color[2], amount)
    alphas = portion(begin_color[3], end_color[3], amount)

    return [(reds[i], greens[i], blues[i], alphas[i]) for i in range(amount)]


def portion(first: int, second: int, amount: int) -> list[int]:
    """Make even divisions between two numbers."""
    div = (first - second) / (amount + 1)

    values = [round(second + (div * (i + 1))) for i in range(amount)]
    values.reverse()

    return values
