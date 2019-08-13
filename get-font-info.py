import fontforge as ff
from sys import argv

def getFontName(font):
    return font.fontname

def getFullName(font):
    return font.fullname

def getSfntProperty(font, property):
    sfntNames = font.sfnt_names
    for entry in sfntNames:
        if property in entry:
            return entry[-1]
            break
    return None

# Regarding family and preferred family, please refer to: https://fontforge.github.io/fontinfo.html

def getFamily(font):
    '''
    Family
        The font's family name
    '''
    return getSfntProperty(font, 'Family')

def getPreferredFamily(font):
    '''
    Preferred Family
        This is to get around a quirk of windows where only four Style names are allowed per family, so font families with more than four styles would get different family names above, but the preferred family name would be the same. This should only be specified if it differs from the family
    '''
    return getSfntProperty(font, 'Preferred Family')

def getWeight(font):
    return font.os2_weight


def main():
    try:
        assert len(argv) > 1
    except AssertionError:
        usageInfo = '[Usage] python2 %s <fontFile>' % __file__
        print(usageInfo)
        exit(1)

    font = ff.open(argv[1])

    fontName = getFontName(font)
    fullName = getFullName(font)
    family = getFamily(font)
    preferredFamily = getPreferredFamily(font)
    weight = getWeight(font)

    print('font name: %s\n'
        'full name: %s\n'
        'family: %s\n'
        'preferred family: %s\n'
        'weight: %s\n'
        % (fontName, fullName, family, preferredFamily, weight)
    )

    font.close()

    pass

if __name__ == '__main__':
    main()
