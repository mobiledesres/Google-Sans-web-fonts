import fontforge as ff
from sys import argv

def getFontFullName(font):
    return font.fullname

def getSfntProperty(font, property):
    sfntNames = font.sfnt_names
    for entry in sfntNames:
        if property in entry:
            return entry[2]
            break
    return None

'''
Regarding family and preferred family, please refer to: https://fontforge.github.io/fontinfo.html

Family
    The font's family name 

Preferred Family
    This is to get around a quirk of windows where only four Style names are allowed per family, so font families with more than four styles would get different family names above, but the preferred family name would be the same. This should only be specified if it differs from the family
'''

def getFamily(font):
    return getSfntProperty(font, 'Family')

def getPreferredFamily(font):
    return getSfntProperty(font, 'Preferred Family')


def main():
    try:
        assert len(argv) > 1
    except AssertionError:
        usageInfo = '[Usage] python2 %s <fontFile>' % __file__
        print(usageInfo)
        exit(1)

    font = ff.open(argv[1])

    fullName = getFontFullName(font)
    family = getFamily(font)
    preferredFamily = getPreferredFamily(font)
    print('full name: %s\nfamily: %s\npreferred family: %s\n' % (fullName, family, preferredFamily))

    font.close()

    pass

if __name__ == '__main__':
    main()
