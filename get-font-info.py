import fontforge as ff
from sys import argv


def get_font_name(font) -> str:
    return font.fontname


def get_full_name(font) -> str:
    return font.fullname


def get_sfnt_property(font, property_name: str) -> str:
    sfnt_names = font.sfnt_names
    for entry in sfnt_names:
        if property_name in entry:
            return entry[-1]
    return ''


# Regarding family and preferred family, please refer to: https://fontforge.github.io/fontinfo.html

def get_family(font) -> str:
    """
    Family
        The font's family name
    """
    return get_sfnt_property(font, 'Family')


def get_preferred_family(font) -> str:
    """
    Preferred Family
    This is to get around a quirk of windows where only four Style names are allowed per family,
    so font families with more than four styles would get different family names above, but the preferred family name
    would be the same.
    This should only be specified if it differs from the family.
    """
    return get_sfnt_property(font, 'Preferred Family')


def get_weight(font):
    return font.os2_weight


def main():
    try:
        assert len(argv) > 1
    except AssertionError:
        usage_info = '[Usage] python2 %s <fontFile>' % __file__
        print(usage_info)
        exit(1)

    with ff.open(argv[1]) as font:

        font_name = get_font_name(font)
        full_name = get_full_name(font)
        family = get_family(font)
        preferred_family = get_preferred_family(font)
        weight = get_weight(font)

        print(
            'font name: %s\n'
            'full name: %s\n'
            'family: %s\n'
            'preferred family: %s\n'
            'weight: %s\n'
            % (font_name, full_name, family, preferred_family, weight)
        )


if __name__ == '__main__':
    main()
