from shade_generator.generator import portion, portion_colors


def test_should_portion_correctly():
    # Single portion
    portions = portion(40, 20, 1)
    assert portions == [30]

    # Multiple portions
    portions = portion(50, 20, 2)
    assert portions == [40, 30]

    # Multiple portions, reversed
    portions = portion(20, 50, 2)
    assert portions == [30, 40]


def test_should_portion_colors():
    colors = portion_colors((20, 20, 20, 20), (50, 50, 50, 50), 2)

    assert len(colors) == 2

    assert colors == [(30, 30, 30, 30), (40, 40, 40, 40)]
