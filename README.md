# Shade Generator

Very simple script to generate colors between two colors. Useful for shading and color easing.

## Requirements

* [Poetry](https://python-poetry.org/docs/#installation)

## Installation

```bash
git clone https://github.com/umutseven92/shade-generator
cd shade-generator
poetry install

```

## Example Usage

To generate two colors between fully opaque red and semi-transparent green:

```bash
poetry run generate --start-color 255 0 0 255 --end-color 0 255 0 120 --amount 2
```

Output:

```bash
Color #1 -> r: 255      g: 0    b: 0    a: 255  hex: #ff0000
Color #2 -> r: 170      g: 85   b: 0    a: 210  hex: #aa5500
Color #3 -> r: 85       g: 170  b: 0    a: 165  hex: #55aa00
Color #4 -> r: 0        g: 255  b: 0    a: 120  hex: #00ff00
```
